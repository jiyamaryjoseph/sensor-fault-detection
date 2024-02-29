from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
from sensor.pipeline import training_pipeline
from sensor.pipeline.training_pipeline import TrainPipeline
import io
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
from fastapi import FastAPI
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
from fastapi import File,UploadFile
import pandas as pd
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from fastapi.responses import JSONResponse


env_file_path=os.path.join(os.getcwd(),"env.yaml")

def set_env_variable(env_file_path):

    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:

        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict")
async def predict_route(data:UploadFile):
    
    try:
        #get data from user csv file
        #conver csv file to dataframe
        content = await data.read()
        
        df = pd.read_csv(io.StringIO(content.decode('utf-8')))
        
        _schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        df = df.drop(_schema_config["drop_columns"],axis=1)
    
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not available")
        
        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        
        df['predicted_column'] = y_pred
        
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(),inplace=True)
        print(df)
        
        predictions=pd.DataFrame(df.index.values,columns=['index'])
       
        predictions['predicted_column'] = df[['predicted_column']]
        
        predictions = predictions.to_dict(orient='records')
        print(predictions)
        
        return JSONResponse(content={"predictions": predictions})
        
    except Exception as e:
        
        return JSONResponse(content={"error": f"An error occurred: {str(e)}"}, status_code=500)

def main():
    try:
        set_env_variable(env_file_path)
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)


if __name__=="__main__":
    # main()
    set_env_variable(env_file_path)
    app_run(app, host=APP_HOST, port=APP_PORT)

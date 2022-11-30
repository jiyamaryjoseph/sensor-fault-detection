from sensor.exception import SensorException
from sensor.entity.artfact_entity import DataIngestionArtifact
from pandas import DataFrame
from sensor.logger import logging
from sensor.data_access.sensor_data import SensorData
import sys,os
from sensor.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            Exception= SensorException(e,sys)
    
    def export_data_into_feature_store(self)->DataFrame:
        """Export MongoDb Data collection record into feautre store"""
        try:
            logging.info("Exporting MongoDb Data collection record into feautre store")
            sensor_data=SensorData()
            dataframe=sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path

            # creating folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True) 

            # save the data
            dataframe.to_csv(feature_store_file_path,index=False,header=True)

            return dataframe


        except Exception as e:
            Exception= SensorException(e,sys)    

    def train_test_split(self,dataframe:DataFrame)->DataFrame:
        """feautre store willl split in to train and test"""
        pass

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            dataframe=self.export_data_into_feature_store()
            self.train_test_split(dataframe=dataframe)
            data_injection_artifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
            test_file_path=self.data_ingestion_config.train_test_split_ratio)
            return data_injection_artifact
        except Exception as e:
            Exception=SensorException(e,sys)
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.configuration import mongo_db_connection
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
import sys


if __name__=='__main__':
    try:
  
        training_pipeline=TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise SensorException(e,sys)

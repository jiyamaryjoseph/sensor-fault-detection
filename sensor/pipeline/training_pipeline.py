from sensor.entity.artfact_entity import DataIngestionArtifact
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.components.data_ingestion import DataIngestion
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys

class TrainPipeline():

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)

    def start_data_ingestion(self)->DataIngestionArtifact:
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
    def start_data_validation(self):
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
    def start_data_tranformation(self):
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
    
    def start_model_trainer(self):
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
    def start_model_evaluation(self):
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
    def start_model_pusher(self):
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
    def run_pipeline(self):
            try:
               pass
            except  Exception as e:
                raise  SensorException(e,sys)
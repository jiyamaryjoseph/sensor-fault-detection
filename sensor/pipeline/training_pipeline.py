from sensor.entity.artfact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from sensor.utils.main_utils import read_yaml_file
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_tranformation import DataTransformation
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH

class TrainPipeline:

    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
        self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

    def start_data_ingestion(self)->DataIngestionArtifact:
            try:
               logging.info("data ingestion started")
               self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
               data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
               data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
               logging.info("Data ingestion completed and artifact:{data_ingestion_artifact}")
               return data_ingestion_artifact
               logging.info("data ingestion topped ")
            except  Exception as e:
                raise  SensorException(e,sys)
    def start_data_validation(self,data_ingestion_artifact=DataIngestionArtifact)->DataValidationArtifact:
            try:
               logging.info("data validation started")
               data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
               data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,
               data_validation_config=data_validation_config)
               data_validation_artifact=data_validation.initiate_data_validation()
               return data_validation_artifact

            except  Exception as e:
                raise  SensorException(e,sys)
    def start_data_tranformation(self,data_validation_artifact:DataValidationArtifact):
            try:
               data_transformation_config=DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
               data_tranformation=DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=data_transformation_config)
               data_tranformation_artifact=data_tranformation.initiate_data_transformation()
               return data_tranformation_artifact


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
               data_ingestion_artifact:DataIngestionArtifact= self.start_data_ingestion()
               data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
               data_tranformation_artifact=self.start_data_tranformation(data_validation_artifact=data_validation_artifact)
            except  Exception as e:
                raise  SensorException(e,sys)
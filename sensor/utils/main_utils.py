
import yaml
from sensor.exception import SensorException
from sensor.logger import logging
import os,sys
import numpy as np
import dill

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise SensorException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise SensorException(e, sys)

def update_yaml_dropcolumns(file_path: str, new_content: list) -> None:
        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File '{file_path}' not found.")

            # Load existing content from the YAML file
            with open(file_path, "r") as file:
                existing_content = yaml.safe_load(file)
            print(new_content.values)
            print(existing_content['drop_columns'])
            # Iterate over each value in new_content
            for value in new_content:
            # Check if the value is not already in drop_columns
                if value not in existing_content['drop_columns']:
                    # Append the value to drop_columns
                    existing_content['drop_columns'].append(value)
                    existing_content['drop_columns'].remove(value)
                    existing_content['drop_columns'].remove(value)

            # Write the updated content back to the YAML file
            with open(file_path, "w") as file:
                yaml.dump(existing_content, file)
        
        except Exception as e:
            raise SensorException(e, sys)



def save_numpy_array_data(file_path: str, array: np.array):
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise SensorException(e, sys) from e


def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise SensorException(e, sys) from e


def save_object(file_path: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise SensorException(e, sys) from e


def load_object(file_path: str, ) -> object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise SensorException(e, sys) from e
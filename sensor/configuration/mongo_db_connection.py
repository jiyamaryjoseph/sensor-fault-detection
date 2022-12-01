import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
from sensor.exception import SensorException
import os,sys
ca=certifi.where()
class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:


        try:
                if MongoDBClient.client is None:

                    mongo_db_url="mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"         #  mongo_db_url = os.getenv(MONGODB_URL_KEY)

                    if mongo_db_url is None:
                        raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")

                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

                self.client = MongoDBClient.client

                self.database = self.client[database_name]

                self.database_name = database_name

        except Exception as e:
            raise SensorException(e, sys)

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifact',"train.csv")
    test_data_path: str=os.path.join('artifact',"test.csv")
    raw_data_path: str=os.path.join('artifact',"data.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
            logging.info("Enter the data ingetion method")
            try:
                df=pd.read_csv('notebook/data/stud.csv')
                logging.info("Read the dataset as dataframe")
                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
                df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
                logging.info("Train test split initiated")
                train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
                train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
                train_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
                logging.info("Ingestion of data is completed")
                return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
                )
            except Exception as e:
                raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
        
# The above code defines a data ingestion class that reads a CSV file, splits it into training and testing sets, and saves them to specified paths. It uses logging for tracking the process and handles exceptions with a custom exception class. The `DataIngestionConfig` dataclass is used to define the configuration for data ingestion, including paths for the train, test, and raw data files.
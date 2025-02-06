import os
from pathlib import Path
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation

@dataclass(frozen=True)
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts/data_ingestion', 'train.csv')
    test_data_path: str=os.path.join('artifacts/data_ingestion', 'test.csv')
    raw_data_path: str=os.path.join('artifacts/data_ingestion', 'data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method")
        try:
            data = pd.read_csv('research/data/stud.csv')
            logging.info("Read the dataset as Dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            data.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(data, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
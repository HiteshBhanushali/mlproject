import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from exception import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngesionConfig:
    train_data_path:str = os.path.join('artifict',"train.csv")
    test_data_path:str = os.path.join('artifict',"test.csv")
    raw_data_path: str = os.path.join('artifict','data.csv')

class DataIngection:
    def __init__(self):
        self.ingection_config = DataIngesionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingection method or component")
        try:
            df = pd.read_csv("notebook\data\stud.csv")

            os.makedirs(os.path.dirname(self.ingection_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingection_config.raw_data_path,index=False,header=True)
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)
            train_data.to_csv(self.ingection_config.train_data_path,index=False,header=True)
            test_data.to_csv(self.ingection_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of the data is completed")
            return(self.ingection_config.test_data_path, self.ingection_config.train_data_path)
        except Exception as e:
            raise CustomException(e,sys)
            
if __name__=="__main__":
    obj = DataIngection()
    obj.initiate_data_ingestion()
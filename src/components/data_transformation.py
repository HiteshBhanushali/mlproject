import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging
from utils import save_object
import os

@dataclass
class DataTransformationConfig():
    preprocessor_obj_file_path = os.path.join('artifict', "preprocessor.pkl")

class DataTransformation():
    def __init__(self):
        self.data_transforamtion_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        '''
        This function is responsibel for data transformation
        '''
        try:
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

            num_pipline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scalar", StandardScaler(with_mean=False))
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scalar", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical Column and Categorical columnEncoding pipleline complete")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipline,numerical_columns),
                    ("cat_pipeline", cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self, train_data_path,test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info("Data read in Transformation complete")
            logging.info("Obtaining preprocessing object")

            preproceesion_obj = self.get_data_transformer_object()

            target_column_name = "math_score"
            numerical_columns = ['reading_score', 'writing_score']

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            
            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(f"applying preprocessing object on training dataframe and testing dataframe.")

            input_feature_train_arr = preproceesion_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preproceesion_obj.transform(input_feature_test_df)
            # print("input_feature_train_arr", input_feature_train_arr[0])
            # print("input_feature_test_arr", input_feature_test_arr[0])
            
            train_arr = np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            logging.info("Saved Processing Object")

            save_object(
                file_path=self.data_transforamtion_config.preprocessor_obj_file_path,
                obj=preproceesion_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_transforamtion_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging
from dataclasses import dataclass

# --------------- Model Import
# Linear Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, HuberRegressor, PassiveAggressiveRegressor, BayesianRidge, ARDRegression

# Tree Models
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Neighbors-based Models
from sklearn.neighbors import KNeighborsRegressor

# Support Vector Machines
from sklearn.svm import SVR

# Ensemble Models
import xgboost as xgb
import lightgbm as lgb
from catboost import CatBoostRegressor



@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifict","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_training_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array, preprocessing_path):
        try:
            logging.info("Started with the model creation")
            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            model ={
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regression":LinearRegression(),
                "K-Neighbour Classification":KNeighborsRegressor(),
                "XGBClassifier":xgb.XGBRegressor(),
                "CatBoosting Classifier":CatBoostRegressor(verbose=False),
                "AdaBoost Classifier": AdaBoostRegressor(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "ElasticNet": ElasticNet(),
                "HuberRegressor": HuberRegressor(),
                "PassiveAggressiveRegressor": PassiveAggressiveRegressor(),
                "BayesianRidge": BayesianRidge(),
                "ARDRegression": ARDRegression(),
                "Support Vector": SVR(),
                "LGBMRegressor": lgb.LGBMRegressor()
            }
        except Exception as e:
            raise CustomException
            

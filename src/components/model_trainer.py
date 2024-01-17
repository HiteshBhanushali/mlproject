import os
import sys
from pathlib import Path

from sklearn.metrics import r2_score
sys.path.append(str(Path(__file__).parent.parent))
from exception import CustomException
from logger import logging
from dataclasses import dataclass
from utils import evaluate_model, save_object
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

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Started with the model creation")
            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models ={
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                "Gradient Boosting":GradientBoostingRegressor(),
                "Linear Regression":LinearRegression(),
                "K-Neighbour Classification":KNeighborsRegressor(),
                "XGBClassifier":xgb.XGBRegressor(),
                "CatBoosting Classifier":CatBoostRegressor(verbose=False),
                # "AdaBoost Classifier": AdaBoostRegressor(),
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

            model_report:dict = evaluate_model(x_train= x_train,y_train=y_train,x_test=x_test,y_test=y_test,
                                               models=models)
            
            ##to get best model score from dict
            # print(model_report.items())
            best_model_score = max(sorted(model_report.values()))
            ## To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]
            if best_model_score<0.6:
                raise CustomException("No Best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path = self.model_training_config.trained_model_file_path,
                obj = best_model
            )
            Predicted = best_model.predict(x_test)
            r2_square = r2_score(y_test,Predicted)
            
            return best_model, r2_square
        except Exception as e:
            raise CustomException(e,sys)
            

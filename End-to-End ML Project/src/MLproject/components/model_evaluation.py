import os
import joblib
import mlflow
import pandas as pd
import numpy as np
from mlflow.sklearn import log_model
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
from pathlib import Path
from MLproject.config.configuration import ModelEvaluationConfig
from MLproject.utils.common import save_json
        
class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
        
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_dir)
        model = joblib.load(self.config.model_dir)
        
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri("https://dagshub.com/Harshvardhan2164/MLOPS-Project.mlflow")
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            
            metrics_dir = os.path.dirname(self.config.metrics_file_name)
            os.makedirs(metrics_dir, exist_ok=True)
            save_json(path=Path(self.config.metrics_file_name), data=scores)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae",mae)
            mlflow.log_metric("r2", r2)
            
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
import os
import pandas as pd
import numpy as np
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.utils import save_object

@dataclass(frozen=True)
class DataTransforamtionConfig:
    preprocessor_obj_file_path: str=os.path.join('artifacts/data_transformation', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransforamtionConfig()

    def get_data_transformer_object(self):
        try:
            numerical_features = ['writing_score', 'reading_score']
            categorical_features = [
                'gender',
                'parental_level_of_education',
                'race_ethnicity',
                'test_preparation_course'
            ]
            
            num_pipeline = Pipeline(
                steps=[
                    ('Imputer', SimpleImputer(strategy='median')),
                    ('Scaler', StandardScaler())
                ]
            )
            
            cat_pipeline = Pipeline(
                steps=[
                    ('Imputer', SimpleImputer(strategy='most_frequent')),
                    ('Encoder', OneHotEncoder()),
                    ('Scaler', StandardScaler(with_mean=False))
                ]
            )
            
            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_features),
                    ('categorical_pipeline', cat_pipeline, categorical_features)
                ]
            )
            
            return preprocessor
            
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info('Trian and Test data Loaded')

            preprocessing_obj = self.get_data_transformer_object()

            target_column = 'math_score'
            
            input_train_df = train_df.drop([target_column], axis=1)
            target_train_df = train_df[target_column]

            input_test_df = test_df.drop([target_column], axis=1)
            target_test_df = test_df[target_column]
            
            logging.info("Applying preprocessing object on training and testing data.")

            input_train_arr = preprocessing_obj.fit_transform(input_train_df)
            input_test_arr = preprocessing_obj.transform(input_test_df)

            train_arr = np.c_[
                input_train_arr, np.array(target_train_df)
            ]
            
            test_arr = np.c_[
                input_test_arr, np.array(target_test_df)
            ]
            
            logging.info("Saved Preprocessing object")

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        
        except Exception as e:
            raise CustomException(e, sys)
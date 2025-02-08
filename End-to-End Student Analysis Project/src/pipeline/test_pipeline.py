import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class TestPipeline:
    def __init__(self):
        pass

    def main(self, features):
        try:
            model_path = os.path.join('artifacts/model_trainer', 'model.pkl')
            preprocessor_path = os.path.join('artifacts/data_transformation', 'preprocessor.pkl')

            print("Before Loading")

            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)

            print("After Loading")

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self, gender:str, race_ethnicity:str, parental_level_of_education:str, test_preparation_course:str, lunch:str, reading_score:str, writing_score:str):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
        
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "lunch": [self.lunch],
                "parental_level_of_education": [self.parental_level_of_education],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score]
            }
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)
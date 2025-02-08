import sys
from src.logger import logging
from src.exception import CustomException
from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.test_pipeline import TestPipeline, CustomData

STAGE_NAME = "Training Stage"

try:
    obj = TrainPipeline()
    obj.main()
    logging.info(f"{STAGE_NAME} Completed.")
except Exception as e:
    raise CustomException(e, sys)

STAGE_NAME = "Testing Stage"

try:
    data = CustomData(
        gender='male',
        race_ethnicity='group C',
        parental_level_of_education='bachelor\'s degree',
        lunch='standard',
        test_preparation_course='completed',
        reading_score=95,
        writing_score=98
    )
    
    pred_df = data.get_data_as_dataframe()
    obj = TestPipeline()
    print(obj.main(pred_df))
    logging.info(f"{STAGE_NAME} Completed")
except Exception as e:
    raise CustomException(e, sys)

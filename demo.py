# # # below code is to check the logging config
# # from src.logger import logging

# # logging.debug("This is a debug message.")
# # logging.info("This is an info message.")
# # logging.warning("This is a warning message.")
# # logging.error("This is an error message.")
# # logging.critical("This is a critical message.")


# # # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e

from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()

# import os
# from datetime import datetime

# # Base directory for artifacts
# TRIAL_DIR = "trial"
# SUB_TRIAL = "sub-trial"

# # Create a timestamp string, e.g. "2025_11_02_14_45_30"
# TIMESTAMP = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

# # Combine them into one path
# trial_dir: str = os.path.join(TRIAL_DIR)

# # Print the result
# print("Trial directory path:", trial_dir)

# # (Optional) Create the directory if it doesn’t exist
# # os.makedirs(trial_dir, exist_ok=True)
# # print("Directory created (if it didn’t already exist).")

# sub_trial: str = os.path.join(trial_dir,SUB_TRIAL)
# os.makedirs(sub_trial, exist_ok=True)


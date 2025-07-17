import logging
import os
from datetime import datetime

LOG_DIR=os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_NAME=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILE_PATH,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')




import os
import sys
import numpy as np
import pickle
from src.exception.exception import CustomException
from src.logging.logger import logging

def save_numpy_array(file_path: str, file: np.ndarray) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as array_file:
            np.save(array_file, file)
        logging.info(f"Numpy array saved successfully at: {file_path}")
    except Exception as e:
        raise CustomException(e, sys)  # type: ignore

def load_numpy_array(file_path: str) -> np.ndarray:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")
        with open(file_path, "rb") as file:
            array = np.load(file)
        logging.info(f"Numpy array loaded successfully from: {file_path}")
        return array
    except Exception as e:
        raise CustomException(e, sys)  # type: ignore

def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved successfully at: {file_path}")
    except Exception as e:
        raise CustomException(e, sys)  # type: ignore

def load_object(file_path: str) -> object:
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")
        with open(file_path, "rb") as obj:
            loaded = pickle.load(obj)
        logging.info(f"Object loaded successfully from: {file_path}")
        return loaded
    except Exception as e:
        raise CustomException(e, sys)  # type: ignore

import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

class DataLoader:
    """handles dataset loading and preprocessing"""
    
    @staticmethod
    def load_csv(filepath):
        if os.path.exists(filepath):
            logging.info(f"loading CSV: {filepath}")
            return pd.read_csv(filepath)
        logging.error(f"file not found: {filepath}")
        return None
    
    @staticmethod
    def load_json(filepath):
        if os.path.exists(filepath):
            logging.info(f"loading JSON: {filepath}")
            return pd.read_json(filepath)
        logging.error(f"file not found: {filepath}")
        return None
    
    @staticmethod
    def load_excel(filepath):
        if os.path.exists(filepath):
            logging.info(f"loading excel: {filepath}")
            return pd.read_excel(filepath)
        logging.error(f"file not found: {filepath}")
        return None
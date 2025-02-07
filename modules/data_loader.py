import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

class DataLoader:
    """handles dataset loading and preprocessing"""

    @staticmethod
    def load_csv(filepath):
        """loading for CSV file"""
        if not os.path.exists(filepath):
            logging.error(f"not found: {filepath}")
            return None

        try:
            logging.info(f"Loading CSV: {filepath}")

            # multiple encodings for flexibility
            for encoding in ["utf-8", "ISO-8859-1", "latin1"]:
                try:
                    df = pd.read_csv(filepath, encoding=encoding)
                    if df.empty:
                        logging.warning(f"file {filepath} is empty.")
                    return df
                except UnicodeDecodeError:
                    logging.warning(f"{encoding} failed for {filepath}, trying next...")

            # fallback code to replace enc
            return pd.read_csv(filepath, encoding="utf-8", errors="replace")

        except Exception as e:
            logging.error(f"error loading CSV {filepath}: {e}")
            return None

    @staticmethod
    def load_json(filepath):
        """loading JSON file"""
        if not os.path.exists(filepath):
            logging.error(f"not found: {filepath}")
            return None

        try:
            logging.info(f"loading JSON: {filepath}")
            df = pd.read_json(filepath)
            if df.empty:
                logging.warning(f"file {filepath} is empty.")
            return df
        except ValueError as e:
            logging.error(f"invalid JSON format in {filepath}: {e}")
            return None
        except Exception as e:
            logging.error(f"error loading JSON {filepath}: {e}")
            return None

    @staticmethod
    def load_excel(filepath):
        """load xlsx file"""
        if not os.path.exists(filepath):
            logging.error(f"not found: {filepath}")
            return None

        try:
            logging.info(f"loading xlsx: {filepath}")
            df = pd.read_excel(filepath)
            if df.empty:
                logging.warning(f"xlsx file {filepath} is empty.")
            return df
        except ValueError as e:
            logging.error(f"invalid file format in {filepath}: {e}")
            return None
        except Exception as e:
            logging.error(f"error loading Excel {filepath}: {e}")
            return None

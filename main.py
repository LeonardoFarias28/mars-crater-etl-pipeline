import pandas as pd
from src.extract.extract import download_data,unzip_file
from src.validate.validate import validate_data
from src.transform.transform import transform_data
from src.load.load import load_data
from config.config import DATA_URL
from playwright.sync_api import  sync_playwright
import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "pipeline.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)


def run_pipeline():

    try:
        logging.info("Starting pipeline...")
        
        # Extract
        with sync_playwright() as playwright:
            try:
                zip_path = download_data(playwright, DATA_URL)
                logging.info("Download completed")
            except Exception as e:
                logging.exception(f"Download failed: {e}")
                raise Exception(f"Download failed: {e}")
                
        logging.info("Starting data extraction...")
        extracted_file = unzip_file(zip_path)
        logging.info("Extraction completed.")

        df = pd.read_csv(extracted_file, sep=",", low_memory=False)

        # Validate
        logging.info("Starting data validation...")
        df = validate_data(df)
        logging.info("Validation completed.")

        # Transform
        logging.info("Starting data transformation...")
        df = transform_data(df)
        logging.info("Transformation completed.")

        # Load
        logging.info("Starting data load...")
        load_data(df)
        logging.info("Data successfully loaded.")

        logging.info("Pipeline finished successfully.")
    except Exception as error:
        logging.exception(f"Pipeline failed: {error}")
        raise Exception(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()
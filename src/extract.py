import pandas as pd
import logging
from typing import Optional

# Setup basic logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(file_path: str) -> Optional[pd.DataFrame]:
    """
    Safely ingest the raw CSV data.
    
    Args:
        file_path (str): Path to the raw CSV file.
        
    Returns:
        pd.DataFrame or None: Returns a DataFrame if extraction is successful and valid, otherwise None.
    """
    logging.info(f"Starting data extraction from: {file_path}")
    try:
        # Read the file using pandas
        df = pd.read_csv(file_path)
        
        # Validate that the required columns for the pipeline exist
        required_columns = ['Branch', 'City', 'Product line', 'Total', 'Rating']
        missing_cols = [col for col in required_columns if col not in df.columns]
        
        if missing_cols:
            logging.error(f"Data validation failed. Missing the following columns: {missing_cols}")
            return None
            
        logging.info("Data extraction and validation successful.")
        return df

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}. Please verify the path is correct.")
        return None
    except Exception as e:
        # Catch any other unexpected errors, such as corrupted files or I/O issues
        logging.error(f"An unexpected error occurred during extraction: {e}")
        return None

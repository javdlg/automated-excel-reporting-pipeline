import logging
import os
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

# Setup basic logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """
    Main orchestration function to run the ETL pipeline.
    """
    logging.info("Starting Automated Excel Reporting Pipeline...")
    
    # Define file paths
    # Using os.path.abspath to ensure paths work regardless of where the script is run from
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "data", "raw", "supermarket-analysis.csv")
    output_path = os.path.join(base_dir, "data", "output", "consolidated_sales_report.xlsx")
    
    # 1. EXTRACT
    logging.info("--- Phase 1: Extraction ---")
    raw_df = extract_data(input_path)
    
    if raw_df is None:
        logging.error("Pipeline aborted during Extraction phase.")
        return
        
    # 2. TRANSFORM
    logging.info("--- Phase 2: Transformation ---")
    processed_data_dict = transform_data(raw_df)
    
    if not processed_data_dict:
        logging.error("Pipeline aborted during Transformation phase. No data to load.")
        return
        
    # 3. LOAD
    logging.info("--- Phase 3: Loading ---")
    success = load_data(processed_data_dict, output_path)
    
    if success:
        logging.info(f"Pipeline completed successfully! Output saved to: {output_path}")
    else:
        logging.error("Pipeline failed during Loading phase.")

if __name__ == "__main__":
    main()

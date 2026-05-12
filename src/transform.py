import pandas as pd
import logging
from typing import Dict

# Setup basic logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names and handle missing values.
    
    Args:
        df (pd.DataFrame): The raw DataFrame.
        
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    logging.info("Starting data cleaning process...")
    # Create a copy to avoid SettingWithCopyWarning
    df_clean = df.copy()
    
    # Standardize column names: lowercase and replace spaces with underscores
    df_clean.columns = [col.lower().replace(' ', '_') for col in df_clean.columns]
    
    # Handle missing values: Fill numeric with 0, categorical with 'Unknown'
    # For this specific dataset, we drop rows where critical columns are missing
    critical_cols = ['branch', 'city', 'product_line', 'total', 'rating']
    initial_shape = df_clean.shape[0]
    df_clean.dropna(subset=critical_cols, inplace=True)
    
    rows_dropped = initial_shape - df_clean.shape[0]
    if rows_dropped > 0:
        logging.warning(f"Dropped {rows_dropped} rows due to missing values in critical columns.")
    
    logging.info("Data cleaning completed successfully.")
    return df_clean

def generate_aggregations(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Calculate key business aggregations.
    
    Args:
        df (pd.DataFrame): The cleaned DataFrame.
        
    Returns:
        Dict[str, pd.DataFrame]: A dictionary containing different aggregated DataFrames.
    """
    logging.info("Starting business aggregations...")
    aggregations = {}
    
    try:
        # 1. Total Revenue by Branch and City
        # Group by branch and city, sum the total revenue
        revenue_by_branch = df.groupby(['branch', 'city'])['total'].sum().reset_index()
        revenue_by_branch.rename(columns={'total': 'total_revenue'}, inplace=True)
        # Sort by total revenue descending
        revenue_by_branch.sort_values(by='total_revenue', ascending=False, inplace=True)
        aggregations['Revenue_by_Branch'] = revenue_by_branch
        
        # 2. Average Customer Rating per Product Line
        avg_rating_product = df.groupby('product_line')['rating'].mean().reset_index()
        avg_rating_product.rename(columns={'rating': 'average_rating'}, inplace=True)
        avg_rating_product['average_rating'] = avg_rating_product['average_rating'].round(2)
        avg_rating_product.sort_values(by='average_rating', ascending=False, inplace=True)
        aggregations['Avg_Rating_by_Product'] = avg_rating_product
        
        # 3. Sales count by Payment method
        # If 'payment' exists, use it, else try 'payment_method' or whatever the column might be
        payment_col = 'payment' if 'payment' in df.columns else 'payment_method' if 'payment_method' in df.columns else None
        
        if payment_col:
            sales_by_payment = df[payment_col].value_counts().reset_index()
            sales_by_payment.columns = ['payment_method', 'transaction_count']
            aggregations['Sales_by_Payment'] = sales_by_payment
        else:
            logging.warning("Payment method column not found. Skipping this aggregation.")
            
        logging.info("Business aggregations completed successfully.")
        
    except Exception as e:
        logging.error(f"An error occurred during aggregation calculations: {e}")
        
    return aggregations

def transform_data(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """
    Main transformation pipeline applying cleaning and aggregations.
    
    Args:
        df (pd.DataFrame): The raw DataFrame.
        
    Returns:
        Dict[str, pd.DataFrame]: A dictionary of processed DataFrames representing report sheets.
    """
    df_clean = clean_data(df)
    final_data_dict = generate_aggregations(df_clean)
    
    return final_data_dict

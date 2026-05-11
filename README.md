# Automated Retail Excel Reporting Pipeline

## Project Overview
This repository contains a robust, production-ready Python pipeline designed to automate repetitive Excel-based workflows. Moving away from fragile macros and manual data entry, this solution uses Python to programmatically extract raw sales data, apply business logic and data cleaning, and generate highly formatted, final Excel reports ready for stakeholder review. The architecture is modular and optimized for agent-assisted development environments (like Antigravity).

## Business Case
A retail company receives daily raw sales data exports in Excel format from multiple regional branches. Currently, data analysts spend hours manually consolidating these files, cleaning formatting errors, calculating key performance indicators (KPIs) such as gross margin and product line revenue, and formatting the final report for the management team. This manual process is time-consuming, unscalable, and highly prone to human error. 

**The Solution:** An automated ETL (Extract, Transform, Load) script that ingests the raw `.xlsx` files, processes the data in memory, and outputs a stylized, consolidated Excel workbook with zero human intervention.

## Objectives
*   **Automate Data Extraction:** Ingest raw Excel datasets reliably, handling missing values and inconsistent formats gracefully.
*   **Data Processing:** Utilize `pandas` to group data, calculate aggregates (e.g., total revenue per product line, average rating per branch), and clean data types.
*   **Automated Formatting:** Use native Excel integration libraries to apply styles, conditional formatting, and auto-adjust column widths in the final output file.
*   **Production Standard:** Deliver an executable, modular `.py` solution avoiding interactive notebooks, ensuring the script can be scheduled or run by non-technical users.

## Tech Stack
*   **Language:** Python 3.10+
*   **Data Manipulation:** `pandas`, `numpy`
*   **Excel Integration:** `openpyxl`, `xlsxwriter` (for advanced formatting and chart generation)
*   **Development Environment:** Antigravity (Agentic IDE)
*   **Version Control:** Git & GitHub

## Project Structure

```text
automated-excel-reporting-pipeline/
├── data/
│   ├── raw/                 # Original Kaggle datasets (e.g., supermarket_sales.xlsx)
│   └── output/              # Generated final reports
├── src/
│   ├── __init__.py
│   ├── extract.py           # Functions to load data and handle I/O errors
│   ├── transform.py         # Business logic, data cleaning, and aggregations using pandas
│   └── load.py              # Excel writing functions, styling, and formatting with openpyxl
├── main.py                  # Main execution script orchestrating the ETL pipeline
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
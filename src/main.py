import pandas as pd 
import logging 

from config import ReportConfig
from load import load_data
from save import save_report
from transform import transform_data
from validate import validate_columns
from report import create_sales_by_category, create_sales_by_region, create_overview, create_returns_by_category

def run_report(config: ReportConfig) -> None:
    data = load_data(config.input_path)

    data = validate_columns(data)

    data = transform_data(data)

    sales_by_category = create_sales_by_category(data)
    sales_by_region = create_sales_by_region(data)
    overview = create_overview(data)
    returns_by_category = create_returns_by_category(data)
    save_report(sales_by_category, config.output_dir / "sales_by_category.csv")
    save_report(sales_by_region, config.output_dir / "sales_by_region.csv")
    save_report(returns_by_category, config.output_dir / "returns_by_category.csv")
    save_report(overview, config.output_dir / "overview.csv")
    
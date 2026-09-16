import pandas as pd

def calculate_total_sales(data: pd.DataFrame) -> float:
    total_sales = round(
            data["discounted_value"].sum(),
            2,
        )
    return total_sales

def calculate_order_count(data: pd.DataFrame) -> int:
    number_of_orders = data["order_id"].nunique()
    return number_of_orders

def calculate_return_count(data: pd.DataFrame) -> int:
    number_of_returns = int(data["returned"].sum())
    return  number_of_returns

def create_overview(data: pd.DataFrame) -> pd.DataFrame:
    total_sales = calculate_total_sales(data)
    number_of_orders = calculate_order_count(data)
    number_of_returns = calculate_return_count(data)
    overview = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )

    return overview


def create_sales_by_category(data: pd.DataFrame) -> pd.DataFrame:
    sales_by_category = (
            data.groupby(
                "product_category",
                as_index=False,
            )
            .agg(
                order_count=("order_id", "nunique"),
                total_sales=("discounted_value", "sum"),
                returns=("returned", "sum"),
            )
        )
    
    sales_by_category["total_sales"] = (
            sales_by_category["total_sales"].round(2)
        )
    
    sales_by_category["return_rate"] = (
            sales_by_category["returns"]
            / sales_by_category["order_count"]
        ).round(3)
    
    sales_by_category = (
            sales_by_category
            .sort_values(
                "total_sales",
                ascending=False,
            )
            .reset_index(drop=True)
        )
    return sales_by_category

def create_sales_by_region(data: pd.DataFrame) -> pd.DataFrame:
    sales_by_region = (
            data.groupby(
                "region",
                as_index=False,
            )
            .agg(
                order_count=("order_id", "nunique"),
                total_sales=("discounted_value", "sum"),
                returns=("returned", "sum"),
            )
        )
    
    sales_by_region["total_sales"] = (
            sales_by_region["total_sales"].round(2)
        )
    
    sales_by_region["return_rate"] = (
            sales_by_region["returns"]
            / sales_by_region["order_count"]
        ).round(3)
    
    sales_by_region = (
            sales_by_region
            .sort_values(
                "total_sales",
                ascending=False,
            )
            .reset_index(drop=True)
        )
    return sales_by_region

def create_returns_by_category(data: pd.DataFrame) -> pd.DataFrame:
    returns_by_category = (
            data.groupby(
                "product_category",
                as_index=False,
            )
            .agg(
                order_count=("order_id", "nunique"),
                returns=("returned", "sum"),
            )
        )
    
    returns_by_category["return_rate"] = (
            returns_by_category["returns"]
            / returns_by_category["order_count"]
        ).round(3)
    
    returns_by_category = (
            returns_by_category
            .sort_values(
                "return_rate",
                ascending=False,
            )
            .reset_index(drop=True)
        )
    return returns_by_category
import pandas as pd

REQUIRED_COLUMNS = {
            "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "discount",
            "returned",
}

def prepare_history(data: pd.DataFrame) -> pd.DataFrame:
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"Sakande kolumner: {missing}")
    return data

def clean_region(data: pd.DataFrame) -> pd.DataFrame:
    data["region"] = (data["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()

        )
    return data 

def clean_product_category(data: pd.DataFrame) -> pd.DataFrame:
    data["product_category"] = (data["product_category"]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .str.title()
        )
    return data 

def clean_quantity(data: pd.DataFrame) -> pd.DataFrame:
    data["quantity"] = pd.to_numeric(
            data["quantity"], errors="coerce"
        ).fillna(1)
    return data 


def clean_unit_price(data: pd.DataFrame) -> pd.DataFrame:
      data["unit_price"] = pd.to_numeric(
            data["unit_price"], errors="coerce"
        ).fillna(data["unit_price"].median())
      return data
    
def clean_discount(data: pd.DataFrame) -> pd.DataFrame:
    data["discount"] = pd.to_numeric(
            data["discount"], errors="coerce"
        ).fillna(0)
    return data 

def clean_returned(data: pd.DataFrame) -> pd.DataFrame:
    data["returned"] = (
        data["returned"]
            .fillna("false")
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["true", "yes", "1", "ja"])
        )
    return data

def calculate_order_values(data: pd.DataFrame) -> pd.DataFrame:
     data["order_value"] = (
            data["quantity"] * data["unit_price"]
        )
     data["discounted_value"] = (
             data["order_value"] * (1 - data["discount"])
         )
     return data 


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    data = prepare_history(data)
    data = clean_region(data)
    data = clean_product_category(data)
    data = clean_quantity(data)
    data = clean_unit_price(data)
    data = clean_discount(data)
    data = clean_returned(data)
    data = calculate_order_values(data)
    return data 
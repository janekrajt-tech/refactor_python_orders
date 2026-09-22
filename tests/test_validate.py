import pandas as pd
import pytest 
from src.validate import validate_columns

def test_validate_columns_with_req_columns():
    data = pd.DataFrame(
        columns = [
             "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "discount",
            "returned",
        ]
    )

    result = validate_columns(data)
    assert result is data 

def test_validate_column_with_miss_column():
    data = pd.DataFrame(
        columns=[
            "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "discount",
        ]
    )

    with pytest.raises(ValueError):
        validate_columns(data)

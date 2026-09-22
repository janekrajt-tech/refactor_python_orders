import pandas as pd

from src.transform import calculate_order_values


def test_calculate_order_values():
    data = pd.DataFrame(
        {
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.10],
        }
    )

    result = calculate_order_values(data)

    assert result["order_value"].iloc[0] == 200
    assert result["discounted_value"].iloc[0] == 180
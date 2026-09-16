import pandas as pd
from pathlib import  Path 

def load_data(input_path: Path) -> pd.DataFrame:
    return pd.read_csv(input_path)
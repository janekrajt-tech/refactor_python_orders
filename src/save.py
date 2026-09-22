import pandas as pd 
from pathlib import Path 
import logging

logger = logging.getLogger(__name__)

def save_report(report: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(path, index=False)
    logger.info("Sparade rapport: %s", path)
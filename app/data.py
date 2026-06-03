import pandas as pd
from typing import Optional

_current_dataframe: Optional[pd.DataFrame] = None

def save_dataframe(df: pd.DataFrame) -> None:
    """Saves a pandas DataFrame globally in memory."""
    global _current_dataframe
    _current_dataframe = df

def get_dataframe() -> Optional[pd.DataFrame]:
    """Retrieves the globally stored pandas DataFrame."""
    global _current_dataframe
    return _current_dataframe
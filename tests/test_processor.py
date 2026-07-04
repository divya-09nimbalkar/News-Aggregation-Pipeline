import pandas as pd
from src.processor import clean_data

def test_processor():
    df = pd.DataFrame({"date": ["2026-06-14", None], "sentiment": [0.5, None]})
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0

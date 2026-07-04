import pandas as pd

def run_analysis(df: pd.DataFrame) -> dict:
    return {
        "articles": len(df),
        "avg_sentiment": df["sentiment"].mean(),
        "sources": df["source"].nunique()
    }

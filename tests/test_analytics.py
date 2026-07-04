import pandas as pd
from src.analytics import run_analysis

def test_analytics():
    df = pd.DataFrame({
        "date": ["2026-06-14"],
        "source": ["BBC"],
        "headline": ["Markets rally"],
        "sentiment": [0.8]
    })
    results = run_analysis(df)
    assert results["articles"] == 1
    assert "avg_sentiment" in results

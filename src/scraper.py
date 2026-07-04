import pandas as pd

def scrape_mock_data() -> pd.DataFrame:
    data = {
        "date": ["2026-06-14", "2026-06-14"],
        "source": ["BBC", "Reuters"],
        "headline": ["Markets rally on crypto news", "Tech stocks dip"],
        "sentiment": [0.7, -0.3]
    }
    return pd.DataFrame(data)

from src.scraper import scrape_mock_data

def test_scraper():
    df = scrape_mock_data()
    assert not df.empty
    assert "headline" in df.columns

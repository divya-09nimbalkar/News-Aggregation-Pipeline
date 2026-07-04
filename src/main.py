from src.utils import log_message
from src.scraper import scrape_mock_data
from src.processor import clean_data
from src.analytics import run_analysis
from src.visualization import plot_sentiment

def main():
    log_message("Starting News Aggregation Pipeline...")
    raw = scrape_mock_data()
    log_message("Scraped data")
    processed = clean_data(raw)
    log_message("Cleaned data")
    results = run_analysis(processed)
    log_message(f"Analysis Results: {results}")
    plot_sentiment(processed)

if __name__ == "__main__":
    main()

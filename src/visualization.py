import matplotlib.pyplot as plt

def plot_sentiment(df):
    df["sentiment"].plot(kind="hist", bins=10, title="Sentiment Distribution")
    plt.show()

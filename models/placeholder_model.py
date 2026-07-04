class PlaceholderModel:
    """
    A placeholder ML model for demonstration.
    Replace this with a real NLP model (e.g., sentiment analysis, topic classification).
    """

    def __init__(self):
        self.name = "PlaceholderModel"

    def predict(self, text: str) -> float:
        """
        Mock prediction: returns a random sentiment score between -1 and 1.
        """
        import random
        return round(random.uniform(-1, 1), 2)

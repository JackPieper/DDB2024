import numpy as np

# Functie om aangepaste nauwkeurigheid te berekenen
def custom_accuracy(y_true, y_pred, tolerance_minutes):
    differences = np.abs(y_true - y_pred)  # Absolute verschillen tussen voorspelde en werkelijke waarden
    tolerance = tolerance_minutes  # Tolerantie in minuten
    accurate_predictions = differences <= tolerance  # Controleer of verschillen binnen tolerantie vallen
    accuracy = np.mean(accurate_predictions) * 100  # Gemiddelde van correcte voorspellingen als percentage
    return accuracy
from sklearn.feature_selection import chi2

from drift_calculator.drift_calculator_base import DriftCalculatorBase


class ChiSquareDriftCalculator(DriftCalculatorBase):
    """Chi Square Calculator for Divergence."""

    def __init__(self):
        return

    def calculate(self, data):
        x = data['x']
        y = data['y']
        chi2_output = chi2(x, y)
        return {"divergence": chi2_output[0].tolist(), "p-value": chi2_output[1].tolist()}

    def get_required_keys(self):
        return ["x", "y"]

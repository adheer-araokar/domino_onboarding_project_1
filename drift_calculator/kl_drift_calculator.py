from math import log2

from drift_calculator.drift_calculator_base import DriftCalculatorBase


class KLDriftCalculator(DriftCalculatorBase):
    """KL Calculator for Divergence."""

    def __init__(self):
        return

    def calculate(self, data):
        x = data['x']
        y = data['y']
        kl_divergence = sum(x[i] * log2(x[i] / y[i]) for i in range(len(x)))
        return {"divergence": [kl_divergence]}

    def get_required_keys(self):
        return ["x", "y"]

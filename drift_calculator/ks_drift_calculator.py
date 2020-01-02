from scipy import stats

from drift_calculator.drift_calculator_base import DriftCalculatorBase


class KSDriftCalculator(DriftCalculatorBase):
    """KS Calculator for Divergence."""

    def __init__(self):
        return

    def calculate(self, data):
        rvs = data['rvs']
        cdf = data['cdf']
        d, p_value = stats.kstest(rvs, cdf)
        return {"divergence": [d], "p-value": [p_value]}

    def get_required_keys(self):
        return ["rvs", "cdf"]

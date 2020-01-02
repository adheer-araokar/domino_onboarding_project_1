from enum import Enum


def get_values():
    """Get a list of String values for all DriftCalculatorType.

    :return: String values for all DriftCalculatorType.
    :rtype: list
    """
    values = []
    for c in DriftCalculatorType:
        values.append(c.value)
    return values


def is_valid_calculator(calculator_name):
    """Checks if input calculator type str is valid, and if so, returns true and it's DriftCalculatorType enum.

    :param calculator_name:
    :returns: bool, DriftCalculatorType
    """
    if calculator_name in get_values():
        return True, DriftCalculatorType(calculator_name)
    return False, None


class DriftCalculatorType(Enum):
    """Describes various types of Drift Calculators.
    """
    KL = "kl"
    KS = "ks"
    CHI_SQUARE = "chi2"

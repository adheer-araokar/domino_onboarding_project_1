from drift_calculator.chi_square_drift_calculator import ChiSquareDriftCalculator
from drift_calculator.drift_calculator_type import DriftCalculatorType
from drift_calculator.kl_drift_calculator import KLDriftCalculator
from drift_calculator.ks_drift_calculator import KSDriftCalculator


def calculate_drift(calculator_type, data):
    """Executor method calling the calculators to calculate the drift.

    :param calculator_type: Type of calculator, String
    :param data: input data, Dict
    :return: Drift
    :rtype: Dict
    """
    calculator = get_drift_calculator(calculator_type)
    if calculator is not None:
        return calculator.calculate(data)
    else:
        raise Exception("No Calculator Found")


def is_input_valid(calculator_type, data):
    """Check if input data is valid or not for a calculator.

    :param calculator_type: Type of calculator, String
    :param data: input data, Dict
    :rtype: bool
    """
    calculator = get_drift_calculator(calculator_type)
    if calculator is not None:
        calculator.is_input_valid(data)
    else:
        raise Exception("No Calculator Found")


def get_drift_calculator(calculator_type):
    """Based on the calculator type mentioned in the input, instantiate and return an impl of DriftCalculatorBase.

    :param calculator_type: Type of calculator, String
    :rtype: DriftCalculatorBase
    """
    if calculator_type == DriftCalculatorType.CHI_SQUARE:
        return ChiSquareDriftCalculator()
    elif calculator_type == DriftCalculatorType.KL:
        return KLDriftCalculator()
    elif calculator_type == DriftCalculatorType.KS:
        return KSDriftCalculator()
    else:
        raise Exception("Calculator type not implemented!")

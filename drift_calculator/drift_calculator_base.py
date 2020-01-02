
class DriftCalculatorBase:

    def calculate(self, data):
        """Calculated the drift.

        :param data: Input Data
        :rtype: Dict
        """
        return

    def is_input_valid(self, data):
        """Checks if the given input has the required keys or not.

        :param data: Input Data
        """
        for key in self.get_required_keys():
            if key not in data.keys():
                raise Exception("Invalid Data! Required keys not present!")

    def get_required_keys(self):
        """Returns [] of keys required in the input data.

        :return: list
        """
        return []



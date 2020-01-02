import connexion

from drift_calculator.drift_calculator_type import is_valid_calculator
from swagger_server.models import DriftRequestPostBody, DriftResponse
from drift_calculator.drift_calculator_executor import calculate_drift, is_input_valid
from flask import Blueprint, Response

api_v1 = Blueprint('api', 'api', url_prefix='/api/v1')


@api_v1.route('/calculate_drift_internal', methods=['GET', 'POST'])
def drift_calculator_request(body=None):  # noqa: E501
    """Internal API that Calculates Drift basis the test type provided in the input on the data.

    :param body: DriftRequestPostBody
    :rtype: Response
    """

    if connexion.request.is_json:
        try:
            body = DriftRequestPostBody.from_dict(connexion.request.get_json())
        except Exception as e:
            return Response(str(e), status=400)
        return drift_calculator_internal(body)  # noqa: E501

    return Response("Invalid Data! Data is not JSON!", status=400)


def drift_calculator_internal(body):
    """Validates data, Calls the calculators and returns the drift.

    :param body: DriftRequestPostBody
    :rtype: DriftResponse
    """
    try:
        drift_calculation_type = body.test_type

        is_valid, test_type = is_valid_calculator(drift_calculation_type)
        if not is_valid:
            return Response("Invalid Calculator Type!", status=400)

        response = {}

        is_input_valid(test_type, body.input_data)

        output = calculate_drift(test_type, body.input_data)
        if output is not None:
            response = DriftResponse(output['divergence'])
            if "p-value" in output.keys():
                response.p_value = output['p-value']
        return response.to_dict()
    except Exception as e:
        return Response(str(e), status=400)

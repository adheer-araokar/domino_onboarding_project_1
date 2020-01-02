import connexion

from swagger_server.models.drift_request_post_body import DriftRequestPostBody  # noqa: E501
from swagger_server.models.drift_response import DriftResponse  # noqa: E501

from controllers.drift_calculator import drift_calculator_internal

import flask


def api_v1_calculate_drift_post(body):  # noqa: E501
    """Calculates Drift basis the test type provided in the input on the data.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: DriftResponse
    """
    if connexion.request.is_json:
        body = DriftRequestPostBody.from_dict(connexion.request.get_json())  # noqa: E501
        return drift_calculator_internal(body)
    return flask.Response("Invalid Data! Data is not JSON!", status=400)

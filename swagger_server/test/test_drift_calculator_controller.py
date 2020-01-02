# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.drift_request_post_body import DriftRequestPostBody  # noqa: E501
from swagger_server.models.drift_response import DriftResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDriftCalculatorController(BaseTestCase):
    """DriftCalculatorController integration test stubs"""

    def test_api_v1_calculate_drift_post(self):
        """Test case for api_v1_calculate_drift_post

        Calculates Drift basis the test type provided in the input on the data.
        """
        body = DriftRequestPostBody()
        response = self.client.open(
            '/api/v1/calculate_drift',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

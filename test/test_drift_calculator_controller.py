# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models import DriftAlgoInputsData, KlInputData
from swagger_server.models.drift_request_post_body import DriftRequestPostBody  # noqa: E501
from swagger_server.models.drift_response import DriftResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDriftCalculatorController(BaseTestCase):
    """drift_calculator.py controller integration test stubs"""

    def test_api_v1_calculate_drift_internal_post_invalid_calculator(self):
        """Test case for api_v1_calculate_drift_post

        Invalid data
        """
        body = DriftRequestPostBody()
        response = self.client.open(
            '/api/v1/calculate_drift_internal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_calculate_drift_internal_post_invalid_type(self):
        """Test case for api_v1_calculate_drift_post

        Invalid test_type
        """
        body = DriftRequestPostBody(test_type="klsa", input_data=DriftAlgoInputsData())
        response = self.client.open(
            '/api/v1/calculate_drift_internal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_calculate_drift_internal_post_invalid_data(self):
        """Test case for api_v1_calculate_drift_post

        Invalid data
        """
        input_data = DriftAlgoInputsData()
        obj = input_data.from_dict({"ab": [1, 2, 3], "y": [11, 22, 33]})
        body = DriftRequestPostBody(test_type="kl", input_data=obj)
        response = self.client.open(
            '/api/v1/calculate_drift_internal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_calculate_drift_internal_post_valid_data_kl(self):
        """Test case for api_v1_calculate_drift_post

        valid data, kl type
        """
        input_data = DriftAlgoInputsData()
        obj = input_data.from_dict({"x": [1, 2, 3], "y": [11, 22, 33]})
        body = DriftRequestPostBody(test_type="kl", input_data=obj)
        response = self.client.open(
            '/api/v1/calculate_drift_internal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_calculate_drift_internal_post_valid_data_ks(self):
        """Test case for api_v1_calculate_drift_post

        valid data, ks type
        """
        input_data = DriftAlgoInputsData()
        obj = input_data.from_dict({"rvs": [1, 2, 3], "cdf": "norm"})
        body = DriftRequestPostBody(test_type="ks", input_data=obj)
        response = self.client.open(
            '/api/v1/calculate_drift_internal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_api_v1_calculate_drift_internal_post_valid_data_chi2(self):
        """Test case for api_v1_calculate_drift_post

        valid data, chi2 type
        """
        input_data = DriftAlgoInputsData()
        obj = input_data.from_dict({"x": [[1, 2, 3], [21, 11, 123]], "y": [1, 2]})
        body = DriftRequestPostBody(test_type="chi2", input_data=obj)
        response = self.client.open(
            '/api/v1/calculate_drift_internal',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

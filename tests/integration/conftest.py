import pytest
import requests

from json import dumps as json_stringify

LAMBDA_URL = '?' # todo:change url


@pytest.fixture
def lambda_function():
    return LambdaFunction


class LambdaFunction:

    @staticmethod
    def call(body):
        cert = ('res/cert.pem', 'res/cert.key')
        headers = {'content-type': 'application/json'}
        response = requests.post(LAMBDA_URL, json_stringify(body), headers=headers, cert=cert)
        return {
            'body': response.text,
            'headers': dict(response.headers),
            'statusCode': response.status_code
        }

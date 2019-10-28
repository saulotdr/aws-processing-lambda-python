import json
import pytest

from json import loads as json_parse


@pytest.fixture
def test_tools():
    return TestTools


class TestTools:

    @staticmethod
    def assert_response_ok(response, body):

        assert response['statusCode'] == 200
        assert body['r'] == 'Ok'

    @staticmethod
    def assert_response_error(response, body):

        assert response['statusCode'] == 400
        assert body['r'] == 'Error'

    @staticmethod
    def assert_response(response):

        assert 'statusCode' in response
        assert type(response['statusCode']) is int

        assert 'headers' in response
        assert type(response['headers']) is dict

        assert 'body' in response
        assert type(response['body']) is str

        headers = dict((h.lower(), v) for h, v in response['headers'].items())
        assert headers['content-type'] == 'application/json'

        body = json_parse(response['body'])
        assert 'r' in body
        assert type(body['r']) is str

        return body

    @staticmethod
    def assert_logger_default_input():
        file = open('res/event_aws.txt')
        assert file is not None or not file

        event = json_parse(file.read())
        assert type(event) is dict
        assert type(event['requestContext']) is dict
        assert event['requestContext']['stage'] == 'qa'
        assert event['requestContext']['requestId'] == '9a294c37-76d2-4ace-b340-0b9c59440d12'

        return event

    @staticmethod
    def assert_logger_stdout(capfd, message):
        capture = capfd.readouterr()
        stdout = capture.out

        assert type(stdout) is str
        assert stdout is not None
        assert message in stdout

    @staticmethod
    def assert_logger_none(capfd):
        capture = capfd.readouterr()
        stderr = capture.err
        stdout = capture.out
        assert type(stdout) is str
        assert stdout is not None
        assert '' in stdout

        assert type(stderr) is str
        assert stderr is not None
        assert '' in stderr


import pytest

from json import dumps as json_stringify
from src.handler import process_event
from src.logger import Logger


@pytest.fixture
def lambda_function():
    return LambdaFunction


@pytest.fixture
def logger_layer():
    return LoggingLayer


class LambdaFunction:

    @staticmethod
    def call(body):
        return process_event({'body': json_stringify(body)}, {})


class LoggingLayer:

    @staticmethod
    def get_logger(event):
        return Logger(event)


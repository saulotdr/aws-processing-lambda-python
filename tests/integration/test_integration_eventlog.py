import pytest

from tests.common import eventlog


def test_ok(test_tools, lambda_function):
    eventlog.test_ok(test_tools, lambda_function)


def test_ok_bigdoc(test_tools, lambda_function):
    eventlog.test_ok_bigdoc(test_tools, lambda_function)


def test_no_rdi(test_tools, lambda_function):
    eventlog.test_no_rdi(test_tools, lambda_function)


def test_invalid_rdi(test_tools, lambda_function):
    eventlog.test_invalid_rdi(test_tools, lambda_function)


def test_no_vb(test_tools, lambda_function):
    eventlog.test_no_vb(test_tools, lambda_function)


def test_invalid_vb(test_tools, lambda_function):
    eventlog.test_invalid_vb(test_tools, lambda_function)

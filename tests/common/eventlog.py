import pytest

from json import loads as parse_json


VALID_RDI = '8cef52f7-0c87-4abe-b53b-a1328bebe381'
INVALID_RDI = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

VALID_VB = [{}]
INVALID_VB = []


def test_ok(test_tools, lambda_function):

    response = lambda_function.call({
        'rdi': VALID_RDI,
        'vb': VALID_VB
    })

    body = test_tools.assert_response(response)
    test_tools.assert_response_ok(response, body)

    assert 'f' in body
    assert 'nST' in body
    assert type(body['nST']) is int


def test_ok_bigdoc(test_tools, lambda_function):

    bigdoc_file = open('res/bigdoc.json')
    bigdoc = parse_json(bigdoc_file.read())

    response = lambda_function.call(bigdoc)

    body = test_tools.assert_response(response)
    test_tools.assert_response_ok(response, body)

    assert 'f' in body
    assert 'nST' in body
    assert type(body['nST']) is int


def test_no_rdi(test_tools, lambda_function):

    response = lambda_function.call({
        'vb': VALID_VB
    })

    body = test_tools.assert_response(response)
    test_tools.assert_response_error(response, body)


def test_invalid_rdi(test_tools, lambda_function):

    response = lambda_function.call({
        'rdi': INVALID_RDI,
        'vb': VALID_VB
    })

    body = test_tools.assert_response(response)
    test_tools.assert_response_error(response, body)


def test_no_vb(test_tools, lambda_function):

    response = lambda_function.call({
        'rdi': VALID_RDI
    })

    body = test_tools.assert_response(response)
    test_tools.assert_response_error(response, body)


def test_invalid_vb(test_tools, lambda_function):

    response = lambda_function.call({
        'rdi': VALID_RDI,
        'vb': INVALID_VB
    })

    body = test_tools.assert_response(response)
    test_tools.assert_response_error(response, body)

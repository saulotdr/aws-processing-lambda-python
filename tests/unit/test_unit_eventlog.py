from logging import DEBUG, ERROR, root

from tests.common import eventlog
from src.processor import Processor


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


def test_partition_key_generation():

    sample_request_id = '156be180-becf-11e9-890a-dfff977ea657'
    event = {'requestContext': {'requestId': sample_request_id}}
    partition_key = Processor.generate_partition_key(event)

    assert type(partition_key) is str
    assert len(partition_key) == 64
    assert partition_key.isalnum()


def test_logger_valid_message_debug(capfd, test_tools, logger_layer):
    root.setLevel(DEBUG)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    message = 'Something happened'
    logger.debug(message)
    test_tools.assert_logger_stdout(capfd, message)


def test_logger_invalid_message_debug(capfd, test_tools, logger_layer):
    root.setLevel(DEBUG)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    logger.debug(None)
    test_tools.assert_logger_none(capfd)


def test_logger_valid_message_valid_payload_debug(capfd, test_tools, logger_layer):
    root.setLevel(DEBUG)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    message = 'Something happened'
    logger.debug(message, payload=valid_input_event)
    test_tools.assert_logger_stdout(capfd, message)


def test_logger_invalid_message_invalid_payload_debug(capfd, test_tools, logger_layer):
    root.setLevel(DEBUG)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    logger.debug(None, payload={'key': 'this is so wrong'})
    test_tools.assert_logger_none(capfd)


def test_logger_valid_message_invalid_payload_debug(capfd, test_tools, logger_layer):
    root.setLevel(DEBUG)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    message = 'Something wrong happened'
    logger.debug(message, payload={'key': 'this is so wrong'})
    test_tools.assert_logger_stdout(capfd, message)


def test_logger_invalid_message_valid_payload_debug(capfd, test_tools, logger_layer):
    root.setLevel(DEBUG)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    logger.debug(None, payload=valid_input_event)
    test_tools.assert_logger_none(capfd)


def test_logger_valid_message_error(capfd, test_tools, logger_layer):
    root.setLevel(ERROR)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    message = 'Something wrong happened'
    logger.error(message)
    test_tools.assert_logger_stdout(capfd, message)


def test_logger_invalid_message_error(capfd, test_tools, logger_layer):
    root.setLevel(ERROR)
    valid_input_event = test_tools.assert_logger_default_input()
    logger = logger_layer.get_logger(valid_input_event)

    logger.error(None)
    test_tools.assert_logger_none(capfd)


def test_logger_valid_message_invalid_payload_error(capfd, test_tools, logger_layer):
    root.setLevel(ERROR)
    valid_input_event = test_tools.assert_logger_default_input()

    logger = logger_layer.get_logger(valid_input_event)
    message = 'Something wrong happened'
    logger.error(message, payload={'key': 'this is so wrong'})
    test_tools.assert_logger_stdout(capfd, message)


def test_logger_invalid_message_valid_payload_error(capfd, test_tools, logger_layer):
    root.setLevel(ERROR)
    valid_input_event = test_tools.assert_logger_default_input()

    logger = logger_layer.get_logger(valid_input_event)
    logger.error(None, payload=valid_input_event)
    test_tools.assert_logger_none(capfd)


def test_logger_valid_message_valid_payload_error(capfd, test_tools, logger_layer):
    root.setLevel(ERROR)
    valid_input_event = test_tools.assert_logger_default_input()

    logger = logger_layer.get_logger(valid_input_event)
    message = 'Something wrong happened'
    logger.error(message, payload=valid_input_event)
    test_tools.assert_logger_stdout(capfd, message)



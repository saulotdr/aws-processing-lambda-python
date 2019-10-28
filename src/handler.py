from json import dumps

from src.logger import Logger
from .processor import Processor
from .constants import HTTP_TOO_MANY_REQUESTS, HTTP_BAD_REQUEST, HTTP_OK

from datetime import datetime, timedelta, timezone
from botocore.exceptions import ClientError
from fastjsonschema.exceptions import JsonSchemaException


def process_event(event, context):
    logger = Logger(event)
    processor = Processor(event, context, logger)
    try:
        processor.validate()
        processor.write_to_kinesis()
        logger.debug('Successfully converted to json', payload=processor.payload)
        return ok()
    except JsonSchemaException as json_exception:  # schema validation failed
        logger.error('Validation error: ' + str(json_exception))
        return nok(HTTP_BAD_REQUEST)
    except ClientError as client_error:  # kinesis error
        logger.error('Client error: ' + str(client_error))
        return nok(HTTP_TOO_MANY_REQUESTS)


def nok(http_code):
    return {
        'statusCode': http_code,
        'body': '{"r":"Error"}',
        'headers': {'content-type': 'application/json'}
    }


def ok():
    success_json = {
        'r': 'Ok'
    }
    return {
        'statusCode': HTTP_OK,
        'headers': {'content-type': 'application/json'},
        'body': dumps(success_json)
    }


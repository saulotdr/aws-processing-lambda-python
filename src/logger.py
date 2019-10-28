import logging

import src.constants as constants
from datetime import datetime, timezone
from sys import stdout
from json import dumps
from copy import deepcopy

"""Root logging configuration"""
handler = logging.StreamHandler(stdout)
handler.setFormatter(logging.Formatter(fmt=''))  # format will be defined in instance level
logging.root.addHandler(handler)
logging.root.setLevel(constants.LOGGING_LEVEL)


class Logger:
    def __init__(self, event):
        self.event = event
        self.logger = logging.getLogger()
        self.default_format, self.json_format = self.create_masks()

    def create_masks(self):
        has_request_context = True if 'requestContext' in self.event else False
        mask = {
            'version': '1.0.0',
            'timestamp': str(datetime.now(timezone.utc)),
            'service': 'aws-lambda-1',
            'env': self.event['requestContext']['stage'] if has_request_context else '',
            'stage': 'processing-handler',
            'region': str(constants.KINESIS_REGION),
            'loggingLevel': '%(levelname)s',
            'requestId': self.event['requestContext']['requestId'] if has_request_context else '',
            'src': '%(filename)s:%(lineno)d',
            'logMessage': '%(message)s'
        }
        json_mask = deepcopy(mask)
        json_mask['json'] = '%(json)s'
        return dumps(mask, indent=4), dumps(json_mask, indent=4)

    @staticmethod
    def change_format(format_type):
        handler.setFormatter(logging.Formatter(fmt=format_type))

    def debug(self, message, payload=None):
        if payload is None or not payload:
            self.change_format(self.default_format)
            self.logger.debug(message)
        else:
            self.change_format(self.json_format)
            self.logger.debug(message, extra={'json': payload})

    def error(self, message, payload=None):
        if payload is None or not payload:
            self.change_format(self.default_format)
            self.logger.error(message)
        else:
            self.change_format(self.json_format)
            self.logger.error(message, extra={'json': payload})


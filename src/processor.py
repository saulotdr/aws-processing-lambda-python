from time import sleep
from os import urandom
from random import randint
from hashlib import sha256
from json import loads as parse_json
from boto3 import client as boto_client
from botocore.exceptions import ClientError

from .validator import validate_payload
from .constants import KINESIS_REGION, KINESIS_ENABLED, KINESIS_STREAM_NAME, RETRY_SECONDS_INTERVAL_FROM, \
    RETRY_SECONDS_INTERVAL_TO, TIMEOUT_SECONDS_THRESHOLD

RETRY_EXCEPTIONS = [
    'ThrottlingException',
    'ProvisionedThroughputExceededException'
]

kinesis_client = boto_client('kinesis', region_name=KINESIS_REGION)


class Processor:

    def __init__(self, event, context, logger):
        self.event = event
        self.context = context
        self.raw_payload = event['body'] if 'body' in event else event
        self.payload = parse_json(self.raw_payload)
        self.logger = logger

    def validate(self):
        validate_payload(self.payload)

    @staticmethod
    def generate_partition_key(event):
        random_bytes = urandom(64)
        request_id = event.get('requestContext', {}).get('requestId', '')
        partition_key = sha256(random_bytes + request_id.encode('utf-8')).hexdigest()
        return partition_key

    def write_to_kinesis(self):
        if KINESIS_ENABLED.lower() != 'true':
            self.logger.debug('Kinesis disabled')
            return

        retries = 1
        while True:
            try:
                kinesis_client.put_record(
                    StreamName=KINESIS_STREAM_NAME,
                    Data=self.raw_payload,
                    PartitionKey=Processor.generate_partition_key(self.event)
                )
                break
            except ClientError as err:
                if self.context.get_remaining_time_in_millis() <= TIMEOUT_SECONDS_THRESHOLD:
                    self.logger.debug('Lambda will reach timeout soon, abort and return error')
                    raise
                if err.response['Error']['Code'] not in RETRY_EXCEPTIONS:
                    self.logger.debug('Unknown exception')
                    raise
                if retries >= 3:
                    self.logger.debug('Maximum retries reached')
                    raise
                sleep(randint(RETRY_SECONDS_INTERVAL_FROM, RETRY_SECONDS_INTERVAL_TO))
                retries += 1

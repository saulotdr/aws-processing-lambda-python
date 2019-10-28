# AWS Log Handler Lambda - using Python 🐍

[![Python version](https://img.shields.io/github/pipenv/locked/python-version/saulotdr/aws-processing-lambda-python?style=for-the-badge)](https://python.org)
[![Known Vulnerabilities](https://snyk.io/test/github/saulotdr/aws-processing-lambda-python/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/saulotdr/aws-processing-lambda-python?targetFile=requirements.txt)

[AWS Lambda](https://aws.amazon.com/lambda/) written in [Python 3.7](https://python.org) to handle logs and send them to Kinesis.

## Flow

1) Lambda function is triggered by API Gateway on route _/log_;
2) Body payload is parsed and validated (minor validations);
3) Record is written to Kinesis Stream.

## Configuration

Environment variables to be configured (all are optional):

| Variable | Description | Default value | Accepted values |
| -------- | ----------- | ------------- | --------------- |
| KINESIS_REGION | Kinesis region in AWS. | **eu-west-1** | **string** |
| KINESIS_STREAM_NAME | Kinesis stream name. | **euqa-klp-elog-stream** | **string** |
| KINESIS_ENABLED | Flag to enable/disable logs to be sent to it. | **(empty or unset means disabled** | **string** |
| RETRY_SECONDS_INTERVAL_FROM | Integer representing the initial interval, in seconds, to wait before retrying | **2** | **positive integer** | 
| RETRY_SECONDS_INTERVAL_TO | Integer representing the maximum interval, in seconds, to wait before retrying | **8** | **positive integer** | 
| LOGGING LEVEL | Logging level to be set | **ERROR** | **"DEBUG" or "ERROR"** | 
| TIMEOUT_SECONDS_THRESHOLD | Integer representing, in seconds, the maximum remaining time before returning 429 HTTP Code | **10** | **positive integer** | 

## Dependencies

You should install [Pipenv](https://docs.pipenv.org), a package tool for Python that simplifies dependency management.

```bash
$ sudo pip3 install pipenv
```

## Build and deploy

Go to the project root folder and run the following command:

```bash
$ ./build 
```

The file `aws-lambda-handler.zip` will be created in project root folder.

This zip package can be deployed directly to AWS Lambda.

## Tests

There are a bunch of types of tests you can run against this Lambda:

- [unit test](tests/unit)
- [integration test](tests/integration)
- [performance test](tests/performance)

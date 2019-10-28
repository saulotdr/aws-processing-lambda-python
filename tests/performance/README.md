# Performance Test

This performance test was designed using [Locust](https://locust.io) - a simple, lightweight and powerful load test framework.

## Plan

Test consists in simulating concurrent requests to the Lambda in order to extract metrics such as average, median, max and min request times, as well as latency, percentiles and more from a **client perspective**.

## Motivation

This test was motivated by the need of having a  performance analysis for Lambdas written in different languages with different runtimes, considering things like request time (average, median and percentiles), number of failures, lambda code and package size.

## Run

Enter following command in performance test folder:

```
$ ./run.sh TIME [USERS] [RATE]
```

- `TIME` time test will run (e.g. 10s, 1h, 20m)
- `[USERS]` (optional) number of concurrent users to simulate
- `[RATE]` (optional) users to ramp per second

## Reports

After running test, reports are saved in `report_*` files in plain CSV format.

## Execution results

Results of tests made before can be found in `test_report.ods` file.

Following params were used:
- 5 minutes of execution
- 10 concurrent users
- 1 user to ramp each second

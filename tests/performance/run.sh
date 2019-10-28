#!/bin/bash

if [ -z $1 ]
then
  echo "
USAGE:  $0 <time> [users] [ramp]

    time   - time test will run (e.g. 10s, 1h, 30m)
    users  - number of concurrent users to simulate (default: 100 users)
    ramp   - users to ramp per second
"
  exit 0
fi

TEST_TIME=$1
TEST_USERS=100
TEST_RAMP=100

if [ ! -z $2 ]; then
  TEST_USERS=$2
fi

if [ ! -z $3 ]; then
  TEST_RAMP=$3
fi

echo "
LOAD TEST

Initializing test with $TEST_USERS users ($TEST_RAMP/s) during $TEST_TIME.
"

locust -f loadtest.py \
  -L INFO \
  --csv=report \
  --only-summary --no-web \
  -c $TEST_USERS -r $TEST_RAMP -t $TEST_TIME

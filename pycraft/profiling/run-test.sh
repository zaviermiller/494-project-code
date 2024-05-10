#!/usr/bin/env bash

# check if python is installed
if ! type python >/dev/null 2>&1; then
    echo "Python is not installed"
    exit 1
fi

# check if nodejs is installed
if ! type node >/dev/null 2>&1; then
    echo "NodeJS is not installed"
    exit 1
fi

# run test 10 times

for value in {1..10}; do
    # run test
    python test.py

    # parse results
    node parse.js >> test-data.csv
done

# compute some stats
# node computeStats.js

# clean up
# rm test-out.tmp
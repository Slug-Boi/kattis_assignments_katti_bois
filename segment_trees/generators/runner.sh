#!/usr/bin/env bash

# This script will run your solution and generate the average time taken to run over N
# Iterations of the test case. You can either provide one solution or TODO pipe the solution generator into this program to get ammortized times
#
# Usage: ./runner.sh <solution> <N> <input>


if [[ -n $1 && -n $2 && -n $3 ]]; then
    solution=$1
    N=$2
    input=$3
else
    echo "Usage: ./runner.sh <solution> <N> <input>"
    exit 1
fi

total=0.00

for i in $(seq 1 $N); do
    start=$(($(gdate +%s%6N)))
    $solution < $input
    end=$(($(gdate +%s%6N)))
    inc=$(($inc + 1))
    total=$(echo "($total + $end - $start)"  | bc)
done

avg=$(echo "($total / $N)"| bc)

echo "Average time taken to run over $N iterations: $avg microseconds"




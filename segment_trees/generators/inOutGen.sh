#!/usr/bin/env bash

# Generate test case
# Usage: python generator.python
#

inc=0

if [[ -n $1 && -n $2 ]]; then
  N=$(($1))
  O=$(($2))
else
   N=$((1 + $RANDOM % 100000))
   O=$((1 + $RANDOM % 1000000))
fi

tst=$(python generator.py $(($N)) $(($O)))

echo "$tst" > "$inc".in

out1=$(python 2_segment_trees.py < "$inc".in) 
out2=$(python group_sol.py < "$inc".in)

if [ "$out1" == "$out2" ]; then
    echo "Correct, printing output to $inc.ans"
    echo "$out1" > "$inc".ans
else 
    echo "Wrong answer"
fi


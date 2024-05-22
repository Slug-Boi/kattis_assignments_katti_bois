#!/usr/bin/env bash

# Generate test case
# Iterations can only be set if left random 
# Usage: python generator.python <iterations>
#

inc=0

I=0

if [[ -n $1 && -n $2 ]]; then
  N=$(($1))
  O=$(($2))
  I=1
else
   N=$((1 + $RANDOM % 100000))
   O=$((1 + $RANDOM % 100000))
   I=$1
fi

for i in $(seq 0 $(($I-1))); do

tst=$(python generator.py $(($N)) $(($O)))

echo "$tst" > inputs/"$inc".in

out1=$(python solutions/2_segment_trees.py < inputs/"$inc".in) 
out2=$(python solutions/group_sol.py < inputs/"$inc".in)

if [ "$out1" == "$out2" ]; then
    echo "Correct, printing output to answers/$inc.ans"
    echo "$out1" > answers/"$inc".ans
    inc=$((inc+1))
else 
    echo "Wrong answer"
fi

done

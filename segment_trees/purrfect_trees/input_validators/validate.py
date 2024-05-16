#!/usr/bin/env python3
import sys
import re

line = sys.stdin.readline()

# Check if the first line is in the correct format
if not re.match(r"^[1-9]\d* [1-9]\d*\n$", line):
    sys.exit(43)

## FIRST LINE CHECKS

# Check if first line is 2 items
inp = line.split()
if len(inp) != 2:
    sys.exit(43)
    
# Check if N and O are integers
N, O = inp   
if not N.isdigit() or not O.isdigit():
    sys.exit(43)

# Check if N and O are within the bounds
if not 1 <= int(N) <= 10**5:
    sys.exit(43)
if not 1 <= int(O) <= 10**6:
    sys.exit(43)


## ARRAY CHECKS

# Check if second line is N integers
arr = []
try:
    arr = list(map(int, sys.stdin.readline().split()))
except:
    sys.exit(43)

# Check if the length of the array is N
if len(arr) != int(N):
    sys.exit(43)

# Check if the integers are within the bounds
for i in arr:
    if not 0 <= i < 10**2:
        sys.exit(43)
        
## QUERY CHECKS
O_actual = 0

while sys.stdin.readline():
    line = sys.stdin.readline()
    # Update the query count
    O_actual += 1
    
    # Check if the query is in the correct format
    if not re.match(r"^[MSU] \d+ \d+$", line):
        sys.exit(43)
    
    ch, n1, n2 = line.split()
    # Check if the queries M and S are within the bounds
    if ch == 'M' or ch == 'S':
        if not (0 <= int(n1) < int(n2) <= int(N)):
            sys.exit(43)
            
    # Check if the queries U are within the bounds
    elif ch == 'U':
        if not (0 <= int(n1) < int(N) and 0 <= int(n2) < 10**2):
            sys.exit(43)
    else:
        sys.exit(43)
        
if O_actual != int(O):
    sys.exit(43)


sys.exit(42)
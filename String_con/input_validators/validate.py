#!/usr/bin/env python3
import sys
import re

line = sys.stdin.readline()
if not re.match(r"(0|[1-9][0-9]*) (0|[1-9][0-9]*) (0|[1-9][0-9]*)\n", line):
    sys.exit(43)
a, b, c = map(int, line.split())
if not (0 <= a <= 10000 and 0 <= b <= 10000 and 0 <= c <= 10000):
    sys.exit(43)
if sys.stdin.readline() != "":
    sys.exit(43)
sys.exit(42)

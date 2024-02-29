#!/usr/bin/env python3
import sys
import re

line = sys.stdin.readline()
if not re.match(r"([A-z1-9][A-z\d]*) ([A-z1-9][A-z\d]*) ([A-z1-9][A-z\d]*) ([A-z1-9][A-z\d]*)", line):
    print("Regex failed")
    sys.exit(43)
a, b, c, d = map(len, line.split())
if not (a <= 64 and b <= 64 and c <= 64 and d <= 64):
    sys.exit(43)
if sys.stdin.readline() != "":
    sys.exit(43)
sys.exit(42)
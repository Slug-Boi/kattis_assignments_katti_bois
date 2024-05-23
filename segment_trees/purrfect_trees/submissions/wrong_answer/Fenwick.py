#!/usr/bin/env python3
def sum(idx, F):
    running_sum = 0
    while idx > 0:
        running_sum += F[idx]
        right_most_set_bit = (idx & -idx)
        idx -= right_most_set_bit
    return running_sum

def add(idx, X, F):
    while idx < len(F):
        F[idx] += X
        right_most_set_bit = (idx & -idx)
        idx += right_most_set_bit

def range_query(l, r, F):
    return sum(r, F) - sum(l, F)

def parser(ch, n1, n2, F):
    if ch == 'S':
        print(range_query(n1,n2, F))
    elif ch == 'U':
        add(n1+1, n2 - range_query(n1, n1+1, F), F)


N, O = map(int, input().split())

arr = list(map(int,input().split()))
arr.insert(0, -1e9)

F = [0] * (N + 1)

# Build the Fenwick tree
for i in range(1, N+1):
    add(i, arr[i], F)

for _ in range(O):
    ch, n1, n2 = input().split()
    parser(ch, int(n1), int(n2), F)


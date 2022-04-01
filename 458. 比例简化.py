from math import gcd

A, B, L = map(int, input().split())
delta = 1e9
_a, _b = 0, 0
for a in range(1, L + 1):
    for b in range(1, L + 1):
        if gcd(a, b) != 1: continue
        x = a / b
        X = A / B
        if x >= X and x - X < delta:
            _a, _b = a, b
            delta = x - X

print(_a, _b)

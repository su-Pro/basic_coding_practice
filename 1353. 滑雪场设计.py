from cmath import cos
from itertools import count
import sys


n = int(input())
H = [int(input()) for x in range(n)]
ans = sys.maxsize

for i in range(17, 101):
    cost, l, r = 0, i - 17, i
    for h in H:
        if l <= h <= r:
            continue
        cost += pow(l - h, 2) if h < l else pow(i - h, 2)
    ans = min(cost, ans)

print(ans)

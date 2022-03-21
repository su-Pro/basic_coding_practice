import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

a, b = map(int, input().strip().split())
c, d = map(int, input().strip().split())
s = b - a + d - c

print(s - max(min(b, d) - max(a, c), 0))

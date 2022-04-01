a = map(int, input().split())
h = int(input()) + 30
print(len(
    [x for x in a if x <= h]
))

N = int(input())
a = set(map(int, input().split()))
print(len(a))
print(
    *sorted(list(a))
)

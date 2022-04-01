n = int(input())
a = list(map(int, input().split()))
for ans in range(0, n):
    if ans in a:
        continue
    print(ans)
    exit()
print(-1)

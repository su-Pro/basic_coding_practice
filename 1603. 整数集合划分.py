N = int(input())
a = list(map(int, input().split()))
len = N // 2
a.sort()
if N % 2 == 0:
    print(
        0,
        sum(a[len:]) - sum(a[:len])
    )
else:
    print(
        1,
        sum(a[len:]) - sum(a[:len])
    )

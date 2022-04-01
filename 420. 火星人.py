from itertools import permutations


n, m = int(input()), int(input())
A = list(map(int, input().split()))


def get_next():
    global A
    # 1. 找到k
    k = n - 2
    while A[k] > A[k + 1]:
        k -= 1
    # 2. 找到比k右侧，和A[k]最接近的位置t
    t = k + 1
    while t < n - 1 and A[t + 1] > A[k]:
        t += 1
    A[k], A[t] = A[t], A[k]
    # 反转k + 1 到 n
    A = A[:k + 1] + A[k + 1:][::-1]


while m:
    get_next()
    m -= 1

print(*A)

N = int(1e3 + 5)
n = int(input())
seq_a = [0] + list(map(int, input().split()))

f = [0] * N


def is_ok(guest_start):
    visited = [False] * N
    f[1] = guest_start
    visited[guest_start] = True

    for i in range(2, n + 1):
        f[i] = seq_a[i - 1] - f[i - 1]
        if f[i] < 1 or f[i] > n: return False
        if visited[f[i]]: return False
        visited[f[i]] = True
    return print(*f[1: n + 1])


for guest_a in range(1, n + 1):
    if is_ok(guest_a): break


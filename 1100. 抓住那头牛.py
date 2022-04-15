import collections
N = int(1e5 + 5)
n, k = map(int, input().split())
dist = [-1] * N


def getDelta(x): return [x - 1, x + 1, x * 2]


def isOK(x): return 0 <= x <= N and dist[x] == -1


def bfs():
    que = collections.deque()
    que.append(n)
    dist[n] = 0
    while que:
        t = que.popleft()
        if t == k:
            return dist[t]
        # 三条边，以当前的代价进行更新
        for nt in getDelta(t):
            if not isOK(nt):
                continue
            dist[nt] = dist[t] + 1
            que.append(nt)
    return dist[k]


print(bfs())



def what_fuck_dp():

    f = [-1] * N
    f[n] = 0

    for i in range(n + 1, k + 1):
        forward_idx = i // 2
        f[i] = f[i - 1] + 1
        if f[forward_idx] != -1:
            f[i] = min(f[i], f[forward_idx] + 1 + (i % 2))

    print(f[k])

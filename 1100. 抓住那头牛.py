import collections

N = int(1e5 + 5)
n, k = map(int, input().split())

dist = [-1] * N


def bfs():
    que = collections.deque()
    que.append(n)
    dist[n] = 0

    while que:
        u = que.popleft()
        if u == k: return dist[u]
        # 扩展三条边
        if u - 1 >= 0 and dist[u - 1] == -1:
            que.append(u - 1)
            dist[u - 1] = dist[u] + 1
        if u + 1 < N and dist[u + 1] == -1:
            que.append(u + 1)
            dist[u + 1] = dist[u] + 1
        if u * 2 < N and dist[u * 2] == -1:
            que.append(u * 2)
            dist[u * 2] = dist[u] + 1
    return -1


print(bfs())

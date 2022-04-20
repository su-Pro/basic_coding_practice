import collections

N, D = 505, float('inf')
g = [[0] * N for x in range(N)]
dist = [D] * N


def ipt(): return map(int, input().split())


def bfs():
    que = collections.deque([1])
    dist[1] = 0
    while que:
        u = que.popleft()
        for v in range(1, n + 1):
            if g[u][v] and dist[v] > dist[u] + 1:
                dist[v] = dist[u] + 1
                que.append(v)
    return dist[n]


m, n = ipt()
for _ in range(m):
    pos = list(map(int, input().split()))
    pos_cnt = len(pos)
    for i in range(0, pos_cnt):
        for j in range(i + 1, pos_cnt):
            g[pos[i]][pos[j]] = True

dist_s = bfs()
if dist_s == D:
    print("NO")
else:
    print(dist_s - 1)

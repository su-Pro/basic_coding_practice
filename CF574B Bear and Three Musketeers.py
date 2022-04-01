# # https://codeforces.com/blog/entry/20040
# import sys
# N, M = 4000 + 10, 4000 + 10
# n, m = map(int, input().split())
# g = [[0] * N for _ in range(N)]
# deg = [0] * N
# for _ in range(m):
#     u, v = map(int, input().split())
#     g[u][v] = 1
#     g[v][u] = 1
#     deg[u] += 1
#     deg[v] += 1

# ans = sys.maxsize

# for x in range(1, n + 1):
#     for y in range(x + 1, n + 1):
#         # we are O(n^2) times here
#         if g[x][y]:
#             # we are O(m) times here
#             for z in range(y + 1, n + 1):
#                 # O(m * n) times here
#                 if g[x][z] and g[y][z]:
#                     ans = min(ans, deg[x] + deg[y] + deg[z])

# print(
#     -1 if ans == sys.maxsize else ans - 6
# )


# 不会TLE的版本
n, m = map(int, input().split())
adj = [0] * n
for i in range(n):
    adj[i] = []
for i in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)
res = int(1e6)
for i in range(n):
    curr = set(adj[i])
    for j in adj[i]:
        for k in adj[j]:
            if k in curr:
                res = min(res, len(adj[i]) + len(adj[j]) + len(adj[k]) - 6)
print(-1 if res == int(1e6) else res)

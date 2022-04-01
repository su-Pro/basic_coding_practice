N = int(input())
deg,ans = [0] * (N + 1),float('-inf')
# 统计度最多的节点，最终结果就是度 + 1
# 因为其他节点均可复用度最多的顶点所用的颜色
for _ in range(1, N):
    u, v = map(int, input().split())
    deg[u] += 1
    deg[v] += 1
    ans = max(ans, max(deg[u], deg[v]))

print(ans + 1)

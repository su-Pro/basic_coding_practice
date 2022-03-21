import collections

n, m = map(int, input().split())


def dfs_solution():
    g = [[] for _ in range(n)]
    for _ in range(m):
        # 建图
        v, u = map(int, input().split())
        g[v - 1].append(u - 1)

    cnt = 0

    # 依次遍历每个节点
    def dfs(node):
        # 已经检查过当前邻居
        if visited[node]: return
        visited[node] = True
        # 遍历所有邻居的邻居的邻居...
        for vv in g[node]: dfs(vv)

    for i in range(n):
        visited = [False] * (n + 1)
        dfs(i)
        cnt += sum(visited)
    print(cnt)


def bfs_solution():
    g, ans = [[] for _ in range(n)], 0
    # 1.build graph
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
    # 2. bfs find every vertex neighbours
    q = collections.deque()
    for i in range(n):
        # note: solution includes self to self! (1 -> 1),so, we count start with 1
        cur_vis_count = 1
        visited = [False] * n
        q.append(i)
        visited[i] = True
        # foreach i's vv
        while q:
            v = q.popleft()
            for vv in g[v]:
                # has been visted!
                if visited[vv]: continue
                # start travel cur vv node
                q.append(vv)
                visited[vv] = True
                cur_vis_count += 1
        ans += cur_vis_count
    print(ans)

# dfs_solution()
# bfs_solution()

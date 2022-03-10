import collections

N = 100010
M = N * 2

# 这里的e 和 ne 代表什么呢？
g, e, ne, idx, in_d = [-1] * N, [0] * M, [0] * M, 0, [0] * N


def add(v_a, v_b):
    global idx
    e[idx] = v_b
    ne[idx] = g[v_a]
    g[v_a] = idx
    idx += 1


n, m = map(int, input().split())

for _ in range(m - 1):
    v1, v2 = map(int, input().split())
    # 建边
    add(v1, v2)
    # 统计入度
    in_d[v2] += 1


def topsort():
    # 1. 寻找拓扑排序的起点：入度为0的点
    q = collections.deque(
        [v for v in in_d if v == 0]
    )
    if not len(q): return False
    # 2. top排序过程中轮训队列,依次做以下事情：
    #     1. 出队头元素，将其相邻节点出度-1
    #     2. 如果当前元素的入度为0，则认为又找到了一个节点，将其入队
    ans = []
    while q:
        node = q.popleft()
        ans.append(q)
        cur = g[node]
        while cur != -1:
            j = e[cur]
            in_d[j] -= 1
            if not in_d[j]:
                q.append(j)
            cur = ne[cur]
    if len(ans) < N:
        return False
    else:
        return "".join(map(str, ans))


top_seq = topsort()
if not top_seq:
    print('-1')
else:
    print(top_seq)

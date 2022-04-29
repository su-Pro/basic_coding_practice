import collections
from array import array


class Bitset(object):
    def __init__(self, N):
        self.unit_cnt = (N // 32) + 1
        self.arr = array('L', [0] * self.unit_cnt)

    def or_op(self, other):
        for i in range(self.unit_cnt):
            self.arr[i] |= other.arr[i]

    def set1(self, i):
        q, d = divmod(i, 32)
        self.arr[q] += (1 << d)

    def count(self):
        ans = 0
        for val in self.arr:
            while val:
                ans += val & 1;
                val >>= 1
        return ans


ipt = lambda: map(int, input().split())

N, M = int(1e5 + 10), int(1e5 + 10)
h, e, ne, idx = [0] * N, [0] * M, [0] * M, 0
in_degree = [0] * N
n, m = ipt()
f = [Bitset(x) for x in range(n + 1)]


def add(u, v):
    global idx
    idx += 1
    e[idx], ne[idx], h[u] = v, h[u], idx


def top_sort():
    sequence, que = [], collections.deque([u for u in range(n) if in_degree[u] == 0])

    while que:
        u = que.popleft()
        sequence.append(u)
        u = h[u]
        while u:
            v = e[u]
            in_degree[v] -= 1
            if in_degree[v] == 0: que.append(v)
            u = ne[u]
    return sequence


for _ in range(m):
    u, v = ipt()
    add(u, v)
    in_degree[v] += 1

top_sequence = top_sort()

# 注意下面要从u开始向临边遍历的时候，如果需要用到诸如f[N] dist[N] 这类的全局状态时，一定要记得先临时存一下u_idx
for u_idx in top_sequence[::-1]:
    f[u_idx].set1(u_idx)
    u = h[u_idx]
    while u:
        v = e[u]
        f[u_idx].or_op(f[v])
        u = ne[u]
for u in range(1,n + 1):
    print(f[u].count())

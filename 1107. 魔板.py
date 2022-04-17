import collections

st, ed = '12345678', ''.join(input().split())
vs, pre_state = {}, {}

C = lambda s: s[0] + s[6] + s[1] + s[3:5] + s[2] + s[5] + s[7]
B = lambda s: s[3] + s[:3] + s[5:] + s[4]
A = lambda s: s[::-1]


def bfs():
    que = collections.deque([st])
    vs[st] = True
    pre_state[st] = ''

    while que:
        u = que.popleft()
        if u == ed: return pre_state[u]
        for v, opt in zip((A(u), B(u), C(u)), ("A", "B", "C")):
            if v in vs: continue
            pre_state[v] = pre_state[u] + opt
            vs[v] = True
            que.append(v)


optPath = bfs()
times = len(optPath)

print(times)
if times > 0: print(optPath)

g = {}

n, m = map(int, input().split())
inDegree = [0] * (n + 1)
topPath = []


def add(v, p):
    global g
    if v in g:
        g[v].append(p)
    else:
        g[v] = [p]


def bfs():
    global inDegree
    queue = [v for v in g.keys() if not inDegree[v]]
    while len(queue):
        v = queue.pop(0)
        topPath.append(v)
        if v not in g: continue
        for neighbour in g[v]:
            inDegree[neighbour] -= 1
            if not inDegree[neighbour]: queue.append(neighbour)


for _ in range(m):
    v, p = map(int, input().split())
    add(v, p)
    inDegree[p] += 1

bfs()

if len(topPath) == n:
    for v in topPath: print(v, end=" ")
else:
    print('-1')

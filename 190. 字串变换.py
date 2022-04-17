import collections

#  TODO: 基础的BFS算法... 如何写？？？？？？？？！！！！！！！！！！
st, ed = input().split()
opt_collection = {}
while True:
    try:
        before, after = input().split()
        if before not in opt_collection:
            opt_collection[before] = [after]
        else:
            opt_collection[before].append(after)
    except:
        break


def bfs():
    que, dist = collections.deque([st]), {}
    dist[st] = 0
    while que:
        u = que.popleft()
        if u == ed: return dist[u]
        for before in opt_collection.keys():
            for after in opt_collection[before]:
                v = u.replace(before, after, 1)
                if v in dist: continue
                dist[v] = dist[u] + 1
                que.append(v)
    return 11


step = bfs()
print(
    "NO ANSWER!" if step > 10 else step
)

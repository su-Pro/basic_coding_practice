import collections

N, n = 105, int(input())
graph, in_degree = collections.defaultdict(list), [0] * N
for u in range(1, n + 1):
    for v in list(map(int, input().split()))[:-1]:
        graph[u].append(v)
        in_degree[v] += 1


def top_sort():
    que, top_sequence = collections.deque(), []
    for u in range(1, n + 1):
        if in_degree[u] == 0: que.append(u)

    while que:
        u = que.popleft()
        top_sequence.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                que.append(v)
    return top_sequence


print(*top_sort())

# TODO: 如何优化呢？
N = 205
n, a, b = map(int, input().split())
pos, vs = [-1] + list(map(int, input().split())), [False] * N

ans = N * N 

def ok(target):
    return 0 <= target < N and not vs[target]


def dfs(layer, cnt):
    global ans
    if layer == b:
        ans = min(ans, cnt)
        return
    for direction in [-1, 1]:
        if layer > n: continue
        target = direction * pos[layer] + layer
        if not ok(target):
            continue
        vs[target] = True
        dfs(target,cnt + 1)
        vs[target] = False

for floor in range(1, n + 1):
    if floor == a:
        dfs(floor, 0)

print(ans if ans != N * N else -1)

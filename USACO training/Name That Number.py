dict = {
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y'],
}
N = input().strip()
ans = []


def dfs(layer, path):

    if layer == len(N):
        ans.append(path.copy())
        return

    for ch in dict[int(N[layer])]:
        path.append(ch)
        dfs(layer + 1, path)
        path.pop()


dfs(0, [])
print(ans)

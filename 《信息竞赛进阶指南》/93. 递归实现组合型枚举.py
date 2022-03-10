
if __name__ == '__main__':
    N = 25
    vt = [False] * N
    n, m = list(map(int, input().split(' ')))

    def dfs(level, path):
        if level == m:
            print(" ".join(map(str, path[1:])))
            return
        for i in range(1, n + 1):
            if i <= path[-1] or vt[i]:
                continue
            vt[i] = True
            path.append(i)
            dfs(level + 1, path)
            path.pop()
            vt[i] = False

    dfs(0, [0])

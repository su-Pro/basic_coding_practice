if __name__ == '__main__':
    N = 10
    vt = [False] * N
    n = int(input())

    def dfs(level, path):
        if level == n:
            print(" ".join(map(str, path)))
            return

        for i in range(1, n + 1):
            if vt[i]:
                continue
            path.append(i)
            vt[i] = True
            dfs(level + 1, path)
            path.pop()
            vt[i] = False

    dfs(0, [])

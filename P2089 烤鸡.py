n = int(input())

if n > 30 or n < 10:
    print(0)
else:
    path = [0] * 10
    ans = []


    def dfs(idx):
        if sum(path) > n: return
        if idx >= 10:
            if sum(path) == n: ans.append(path.copy())
            return
        for i in range(1, 3 + 1):
            path[idx] = i
            dfs(idx + 1)
            path[idx] = 0

    def printAns():
        print(len(ans))
        for a in ans:
            print(*a)


    dfs(0)
    printAns()

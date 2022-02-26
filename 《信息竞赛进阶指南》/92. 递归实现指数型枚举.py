N = 20
vt = [False] * N


def dfs(level, path):
    # 相当于把整个搜索树的每个节点都进行一次打印
    print(" ".join(map(str, path[1:])))
    if level == n:
        return
    # 加当前数字以及不加
    for i in range(1, n + 1):
        if i <= path[-1] or vt[i]:
            continue
        path.append(i)
        vt[i] = True
        dfs(level + 1, path)
        vt[i] = False
        path.pop()


if __name__ == '__main__':
    n = int(input())
    dfs(0, [0])

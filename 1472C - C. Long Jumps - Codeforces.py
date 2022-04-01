t = int(input())


def do(n, a):
    # try evey pos
    ans = 0
    vs = [False] * n
    for i in range(n):
        # correct reduce
        if vs[i]: continue
        j = i
        cnt = 0
        while j < n:
            vs[j] = True
            cnt += a[j]
            j = a[j] + j
        ans = max(ans, cnt)
    return ans


if __name__ == '__main__':
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(do(n, a))

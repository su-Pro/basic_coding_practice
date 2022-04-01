def smart():
    a, b = map(int, input().split())
    path = [b]
    while b != a:
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            break

        if b < a:
            break
        else:
            path.insert(0, b)
    if a == b:
        print("YES", len(path), " ".join(map(str, path)), sep="\n")
    else:
        print("NO")


def bruteForce():
    a, b = map(int, input().split())
    path = [a]

    def dfs(a):
        if a == b:
            print("YES", len(path), ' '.join(map(str, path)), sep="\n")
            exit()
        elif a > b:
            return
        else:
            for d_a in (a * 10 + 1, a * 2):
                path.append(d_a)
                dfs(d_a)
                path.pop()
    dfs(a)
    print("NO")


# bruteForce()
smart()

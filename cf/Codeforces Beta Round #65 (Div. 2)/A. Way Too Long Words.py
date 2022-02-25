N = int(input())


def abbreviation(s):
    return s[0] + str(len(s[1:-1])) + s[-1]


for _ in range(N):
    s = input()
    if len(s) > 10:
        print(abbreviation(s))
    else:
        print(s)

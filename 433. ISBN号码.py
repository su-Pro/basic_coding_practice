a = input()
target = a[-1]


def getRight():
    num = 1
    ans = 0
    for ch in a[:-1]:
        if ch != '-':
            ans += int(ch) * num
            num += 1
    ans %= 11
    return str(ans) if ans < 10 else 'X'


my_target = getRight()
print("Right" if target == my_target else a[:-1] + my_target)

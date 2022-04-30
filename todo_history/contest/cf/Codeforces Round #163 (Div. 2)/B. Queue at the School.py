N, T = list(map(int, input().split()))
q = list(input())


# 循环修改多少次？
def check_swap(q):
    i = len(q) - 1
    # 分情况讨论交换和不交换后所做的事情。
    while i >= 1:
        if q[i] == 'G' and q[i - 1] == "B":
            q[i], q[i - 1] = q[i - 1], q[i]
            i -= 2
        else:
            i -= 1


for _ in range(T):
    # 从后向前两个一组进行检查
    check_swap(q)

print("".join(q))

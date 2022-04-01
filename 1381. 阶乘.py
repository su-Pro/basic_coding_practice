n = int(input())
res, d2, d5 = 1, 0, 0

for i in range(1, n + 1):
    x = i
    while x % 2 == 0:
        x //= 2
        d2 += 1
    while x % 5 == 0:
        x //= 5
        d5 += 1
    # 到这里的时候，x 如果原本是10，分解完毕后就是1，不会对结果有影响
    # 所以可以证明上面两个提取2和5质因数过程能够消除末尾0
    res = res * x % 10

k = min(d2, d5)
# 把约掉分母10^k 后剩余的2和5乘到答案中
for i in range(d2 - k):
    res = res * 2 % 10
for i in range(d5 - k):
    res = res * 5 % 10

print(res)

N,M = map(int,input().split())

A,B,G = [0] * 151,[0] * 151,[0] * 101
for i in range(M):
    u,v = map(int,input().split())
    A[i] = u
    B[i] = v
    if A[i] > B[i]:
        A[i],B[i] = B[i],A[i]
# A B 存储图中的边关系

# 依次尝试每块草坪可以染的颜色
for i in range(1,N + 1):
    g = 0
    for _g in range(1, 5):
        ok = True
        for j in range(M):
            if B[j] == i and G[A[j]] == _g: ok = False
        if ok: 
            g = _g
            break
    G[i] = g
    print(g,end='')

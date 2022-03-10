N = int(input())
out_deg,res = [0] * (N + 1),-1

for i in range(1,N):
    u,v = map(int,input().split())
    out_deg[u] += 1

for i in range(1,N + 1):
    # 性质二不满足
    if out_deg[i] == 0 and res != -1:
        res = -1
        break
    if out_deg[i] == 0:
        res = i

print(res)
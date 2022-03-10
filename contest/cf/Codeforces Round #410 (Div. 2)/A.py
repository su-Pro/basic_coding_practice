S = input()
l_s = len(S)
l, r, cnt = 0, l_s - 1, 0
for i in range(l_s // 2):
    if S[i] != S[l_s - i - 1]: cnt += 1

if cnt == 0 and l_s % 2 != 0 or cnt == 1:
    print("YES")
else:
    print("NO")

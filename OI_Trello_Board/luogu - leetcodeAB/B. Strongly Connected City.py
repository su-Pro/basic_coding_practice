n, m = map(lambda v: int(v) - 1, input().split())
din, dim = [0] * 22, [0] * 22
# read grid
for i, c in enumerate(input()):
    if c == '>':
        din[i] = 1
for i, c in enumerate(input()):
    if c == '^':
        dim[i] = 1

flag = True
if din[0] != dim[0]:
    flag = False
if din[0] == dim[m]:
    flag = False
if din[n] == dim[0]:
    flag = False
if din[n] != dim[m]:
    flag = False
print("YES" if flag else "NO")

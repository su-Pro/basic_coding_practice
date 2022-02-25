s = input()
hello, h_idx = 'hello', 0

for ch in s:
    if h_idx == len(hello): break
    if ch == hello[h_idx]:
        h_idx += 1

if h_idx == len(hello):
    print("YES")
else:
    print("NO")

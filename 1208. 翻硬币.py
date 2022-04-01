a, b = list(input()), list(input())

ans, idx = 0, 0
while idx < len(a) - 1:
    if a[idx] != b[idx]:
        a[idx + 1] = '*' if a[idx + 1] == 'o' else 'o'
        ans += 1
    idx += 1

print(ans)

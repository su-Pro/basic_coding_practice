N = int(input())
p, h, s = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)

for i in range(1, N + 1):
    p[i] = p[i - 1]
    h[i] = h[i - 1]
    s[i] = s[i - 1]
    c = input()
    if c == 'P':
        p[i] += 1
    elif c == 'H':
        h[i] += 1
    else:
        s[i] += 1

ans = 0

for i in range(1, N + 1):
    update = lambda x, y: max(ans, x[i] + (y[N] - y[i]))
    ans = update(p, h)
    ans = update(p, s)
    ans = update(h, p)
    ans = update(h, s)
    ans = update(s, p)
    ans = update(s, h)

print(ans)

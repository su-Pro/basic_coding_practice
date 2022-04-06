n = int(input())
if n < 3:
    print(n)
else:
    a, b = 1, 2
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print(b)

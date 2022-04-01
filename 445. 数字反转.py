a = int(input())
if a > 0:
    b = str(a)[::-1]
    b = b.lstrip('0')
    print(b)
elif a < 0:
    b = str(a)[1:][::-1]
    b = b.lstrip('0')
    print('-' + b)
else:
    print(0)

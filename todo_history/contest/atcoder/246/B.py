a, b = map(int, input().split())
x, y = 0, 0
if a == 0 or b == 0:
    x, y = a, b
else:
    temp = a / b
    
print('%.12f' % x,end=' ')
print('%.12f' % y,end=' ')

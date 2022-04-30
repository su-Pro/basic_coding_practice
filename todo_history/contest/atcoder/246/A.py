x,y = 0,0
for i in range(3):
    _x,_y = map(int,input().split())
    x ^= _x
    y ^= _y

print(x,y)

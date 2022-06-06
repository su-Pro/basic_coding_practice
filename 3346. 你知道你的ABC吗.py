ipt = lambda: map(int,input().split())

number_collections = list(ipt())

number_collections.sort()

a,b = number_collections[0],number_collections[1]
c = number_collections[-1] - a - b

print(a,b,c)
a, b, c, d = map(int, input().split())

totalA = a * 60 + b
totalB = c * 60 + d + 1
if totalA < totalB:
    print("Takahashi")
else:
    print("Aoki")

import collections


N, M = map(int, input().split())
nums = list(map(int, input().split()))
h = {}
a, b = int(10e5) + 1, 0

for i in range(1, len(nums)):
    h[M - nums[i - 1]] = True
    if nums[i] in h:
        # update answer
        _a, _b = M - nums[i], nums[i]
        if _a > _b:
            _a, _b = _b, _a
        # 答案要更小的a
        if _a < a:
            a, b = _a, _b

if a == int(10e5) + 1:
    print('No Solution')
else:
    print(a, b)

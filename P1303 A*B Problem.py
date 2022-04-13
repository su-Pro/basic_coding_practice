numA = list(map(int, input().split()))[::-1]
numB = list(map(int, input().split()))[::-1]  # list(map(int, input())).reverse()会报错。

result = []
for i, vala in enumerate(numA):
    for j, valb in enumerate(numB):
        if i + j < len(result):
            result[i + j] += vala * valb
        else:
            result.insert(i + j, vala * valb)

index = 0
while index < len(result):
    # 最后一位是零时表示已经进位完毕了
    if index == len(result) - 1 and result[index] == 0:
        break
    if index + 1 < len(result):
        result[index + 1] += int(result[index] / 10)
    else:
        result.insert(index + 1, int(result[index] / 10))
    result[index] = result[index] % 10
    index += 1

print(''.join(map(str, result[::-1][1:])))
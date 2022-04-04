n, m = map(int, input().split())
square_cnt, oblong_cnt = 0, 0

for i in range(n):
    for j in range(m):
        cur_rectangle, cur_square = (n - i) * (m - j), min(n - i, m - j)
        oblong_cnt += cur_rectangle - cur_square
        square_cnt += cur_square

print(square_cnt, oblong_cnt)

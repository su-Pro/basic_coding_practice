"""
ID: supyyy21
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

N = int(fin.readline().strip())
intervals = [tuple(map(int, fin.readline().strip().split())) for x in range(N)]
# 以左端点进行排序
intervals.sort(key=lambda v: v[0])
max_l, max_g = 0, 0

l, r = intervals[0]
for i in range(1, len(intervals)):
    new_l, new_r = intervals[i]
    if new_l <= r:
        r = max(new_r, r)
    else:
        max_l = max(max_l, r - l)
        max_g = max(max_g, new_l - r)
        l, r = new_l, new_r

max_l = max(max_l, r - l)
fout.write(f"{max_l} {max_g}")
fout.write('\n')
fout.close()

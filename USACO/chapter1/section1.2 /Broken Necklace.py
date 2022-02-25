"""
ID: supyyy21
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

N = int(fin.readline().strip())
s = fin.readline().strip()
s = s + s


def to_bin(c):
    return 2 if c == 'r' else 1


ans = 0

for i in range(N):
    l, r, cnt = i, N + i - 1, 0
    bin_l, bin_r = 0, 0
    # collect left
    while l <= r and (s[l] == 'w' or bin_l | to_bin(s[l]) != 3):
        if s[l] != 'w': bin_l |= to_bin(s[l])  # marked color
        cnt += 1
        l += 1
    # collect right
    while l <= r and (s[r] == 'w' or bin_r | to_bin(s[r]) != 3):
        if s[r] != 'w': bin_r |= to_bin(s[r])  # marked color
        cnt += 1
        r -= 1
    # update ans
    ans = max(ans, cnt)

fout.write(str(ans))
fout.write('\n')
fout.close()

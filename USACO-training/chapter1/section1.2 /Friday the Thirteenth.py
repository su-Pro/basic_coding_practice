"""
ID: supyyy21
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

N = int(fin.readline().strip())
months, weeks = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], [0] * 7
y, d = 1900, 0

for _ in range(N):
    for m_idx in range(1,13):
        weeks[(d + 12) % 7] += 1
        d += months[m_idx]
        if m_idx == 2 and (y % 400 == 0 or (y % 4 == 0 and y % 100)):
            d += 1
    y += 1

for idx, _ in enumerate(weeks):
    fout.write(f"{weeks[(idx - 2)]}")
    if idx <= 5:
        fout.write(f" ")

fout.write('\n')
fout.close()

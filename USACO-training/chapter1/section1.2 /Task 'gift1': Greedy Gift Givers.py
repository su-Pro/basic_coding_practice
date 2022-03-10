"""
ID: supyyy21
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

N = int(fin.readline().strip())
friends = dict.fromkeys([fin.readline().rstrip() for x in range(N)], 0)


def do_gift(oneself, sum_money, n_p, friends):
    # 不会对大家最终收益有任何影响的情况：
    if n_p == 0 or sum_money == 0:
        average = 0
    else:
        average = sum_money // n_p
    for _ in range(n_p):
        friends[fin.readline().rstrip()] += average
    friends[oneself] -= average * n_p


for _ in range(N):
    p = fin.readline().rstrip()
    sum_money, n_p = map(int, fin.readline().strip().split())
    do_gift(p, sum_money, n_p, friends)

for k, v in friends.items():
    fout.write(f"{k} {str(v)}\n")
fout.close()

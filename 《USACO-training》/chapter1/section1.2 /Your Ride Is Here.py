"""
ID: supyyy21
LANG: PYTHON3
PROG: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

ride_name = fin.readline()
group_name = fin.readline()


def name2Ascii(a):
    cnt = 1
    for c in a:
        cnt *= ord(c) - ord('@')
    return cnt % 47


ans = name2Ascii(ride_name) == name2Ascii(group_name)

fout.write("GO" if ans else "STAY")
fout.write('\n')
fout.close()

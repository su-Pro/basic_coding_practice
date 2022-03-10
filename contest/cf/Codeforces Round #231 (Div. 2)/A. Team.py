N = int(input())

cnt = 0


def isOK(problem_line):
    return problem_line.count('1') >= 2

for _ in range(N):
    problem = input()
    if isOK(problem):
        cnt += 1

print(cnt)
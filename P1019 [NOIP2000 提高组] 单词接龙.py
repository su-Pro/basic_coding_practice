N = int(input())
words = [input() for x in range(N)]
begin = input()
coress_d = [[0] * N for x in range(N)]
ans, vs = 0, [2] * N


def dfs(prev_word_idx, prev_length):
    ans = max(ans, prev_length)
    # 尝试所有单词
    for i, w in enumerate(words):
        if can_not_select(prev_word_idx, i):
            continue
        vs[i] -= 1
        dfs(i, prev_length + len(w) - coress_d[prev_word_idx][i])
        vs[i] += 1


# finding firstly selected word
for i, w in enumerate(words):
    if w[0] == begin:
        vs[i] -= 1
        dfs(i, len(w))
        vs[i] += 1

print(ans)

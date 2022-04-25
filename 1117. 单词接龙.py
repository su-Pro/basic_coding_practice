N, n = 20, int(input())
word_collection, used_time, dragon_start = [
    input() for x in range(n)], [0] * N, input()

ans, overlap = 0, [[0] * N for x in range(N)]

# 预处理龙之间的重叠开始索引
for i, w1 in enumerate(word_collection):
    for j, w2 in enumerate(word_collection):
        for k in range(1, min(len(w1), len(w2)) + 1):
            if w1[len(w1) - k:] == w2[:k]:
                # 做一次即可，因为相交越小，龙长度越大
                # abcabc
                # ab
                # =====> 相交长度取2
                overlap[i][j] = k
                break


def depth_first_search(dragon_str, pre_word_idx):
    global ans
    ans = max(ans, len(dragon_str))
    # TODO: 恢复现场的时机： for循环里面和外面 分别有什么说法？
    used_time[pre_word_idx] += 1
    # 尝试每个单词拼接龙
    for cur_word_idx in range(n):
        overlap_start = overlap[pre_word_idx][cur_word_idx]
        if used_time[cur_word_idx] < 2 and overlap_start > 0:
            depth_first_search(
                dragon_str + word_collection[cur_word_idx][overlap_start:], cur_word_idx)
    used_time[pre_word_idx] -= 1


for idx, word in enumerate(word_collection):
    if word[0] == dragon_start:
        depth_first_search(word, idx)

print(ans)

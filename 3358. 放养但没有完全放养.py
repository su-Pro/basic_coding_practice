custom_order_dist = [0] * 26
chToNumber = lambda ch: ord(ch) - ord('a')

for idx,ch in enumerate(input()):
    custom_order_dist[chToNumber(ch)] = idx

song, ans = list(input()), 1

for idx in range(1, len(song)):
    if custom_order_dist[chToNumber(song[idx - 1])] >= custom_order_dist[chToNumber(song[idx])]:
        ans += 1

print(ans)

vowels = ["a", "o", "y", "e", "u", "i"]

s = input().lower()

ans = ''
for ch in s:
    if ch in vowels: continue
    ans += '.'
    ans += ch

print(ans)

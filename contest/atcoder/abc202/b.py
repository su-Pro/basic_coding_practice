S = list(input())
ans = ""
for ch in S[::-1]:
    if ch == "6":
        ans += '9'
    elif ch == '9':
        ans += '6'
    else:
        ans += ch

print(ans)

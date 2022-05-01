class Solution:
    def removeDigit(self, s: str, d: str) -> str:
        solution = [
            s[i:] + s[i + 1:] for i, ch in enumerate(s) if ch == d
        ]
        return max(solution)


print(max(['1', '10']))
print(max(['a', 'b']))
print(max(['aaa', 'b']))

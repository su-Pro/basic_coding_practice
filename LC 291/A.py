class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0
        for i in range(len(number)):
            if digit == number[i]:
                ans = max(ans, int(number[:i] + number[i + 1:]))
        return str(ans)

Solution().removeDigit(
    '133235',
    '3'
)

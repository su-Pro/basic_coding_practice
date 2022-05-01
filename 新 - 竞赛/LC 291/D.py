class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for x in range(n)]

        for i in range(n):
            f[i][i] = 1

        for l in range(n - 1):
            ch = set()
            ch.add(s[l])
            for r in range(l + 1, n):
                f[l][r] = f[l][r - 1] + (s[r] not in ch)
                ch.add(s[r])
        ans = 0
        for row in f:
            ans += sum(row)
        print(ans)


Solution().appealSum(
    # 'code'
"abbca"
)

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0: return target - 1
        if target == 1: return 0
        cnt = 0
        while maxDoubles > 0:
            if target <= 2: break
            if target % 2 != 0: cnt += 1
            target = target // 2
            cnt += 1
            maxDoubles -= 1
        cnt += target - 1
        return cnt


s = Solution()
#
print(s.minMoves(10, 4))
print(s.minMoves(19, 2))
print(s.minMoves(5, 0))
print(s.minMoves(5, 6))
print(s.minMoves(1, 100))
print(s.minMoves(2, 100))
print(s.minMoves(
    230308117,
    32))

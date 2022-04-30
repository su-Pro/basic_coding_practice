class Solution:
    def countCollisions(self, directions: str) -> int:
        cnt = 0
        directions = list(directions)
        for i in range(1, len(directions)):
            if directions[i] == 'L' and directions[i - 1] == 'R':
                cnt += 2
                directions[i] = 'S'
            elif directions[i] == 'L' and directions[i - 1] == 'S':
                cnt += 1
                directions[i] = 'S'
            elif directions[i] == 'S' and directions[i - 1] == 'R':
                cnt += 1
        print(cnt)
        return cnt

Solution().countCollisions("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")
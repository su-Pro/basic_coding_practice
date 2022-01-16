from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ret = []
        s = list(s)
        tempK = k
        while 0 < k <= len(s):
            temp = []
            for _ in range(tempK):
                if len(s) == 0: break
                temp.append(s.pop(0))
            ret.append(''.join(temp))
            k -= 1
        if s[-1] != tempK:
            s[-1] = s[-1] + fill * tempK - len(s[-1])
            print(s[-1])
        if len(s) > 0:
            ret.append("".join(s + [fill] * (tempK - len(s))))
        print(ret)
        return ret



s = Solution()

s.divideString("abcdefghig",3,'x')
s.divideString("jzfysstcjcciyb",5,'n')

from typing import List


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h_a, m_a = current.split(":")
        h_b, m_b = correct.split(":")

        time_a = int(h_a) * 60 + int(m_a)
        time_b = int(h_b) * 60 + int(m_b)

        cnt = 0
        while time_a != time_b:
            if time_a + 60 <= time_b:
                time_a += 60
            elif time_a + 15 <= time_b:
                time_a += 15
            elif time_a + 5 <= time_b:
                time_a += 5
            elif time_a + 1 <= time_b:
                time_a += 1
            cnt += 1
        return cnt
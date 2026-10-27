class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        m = [1,2]
        for i in range(2, n):
            m.append(m[i-1]+m[i-2])
        return m[-1]
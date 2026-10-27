class Solution:
    def trap(self, height: List[int]) -> int:
        c = 0
        lr = []
        rl = []
        for i in height:
            c = max(c,i)
            lr.append(c)
        c = 0
        for i in range(len(height)-1, -1,-1):
            c = max(c,height[i])
            rl.append(c)
        rl.reverse()
        rez = 0
        for i in range(0,len(height)):
            rez = rez + min(lr[i],rl[i])-height[i]
        return rez
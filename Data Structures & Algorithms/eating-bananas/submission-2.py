class Solution:

    def calc(self,piles,k):
        import math
        p = 0
        for i in piles:
            p = p + math.ceil(i/k)
        return p


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while(l<=r):
            mid = (r-l)//2+l
            if self.calc(piles,mid)>h:
                l=mid+1
            else:
                r=mid-1
        return l
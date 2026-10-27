class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        rez =0
        j = len(heights)-1
        while i<j:
            area = min(heights[i],heights[j])*(j-i)
            rez = max(area,rez)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return rez
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        q = []
        for i in nums:
            heapq.heappush(q,(i,i))
        for i in range(1,len(nums)-k+1):
            heapq.heappop(q)
        a,b= heapq.heappop(q)
        return a
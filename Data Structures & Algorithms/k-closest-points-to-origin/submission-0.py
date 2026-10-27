class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        q = []
        for p in points:
            distance = math.sqrt(((0 - p[0])**2 + (0 - p[1])**2))
            #print(p,distance)
            heapq.heappush(q,(distance,p))
        rez = []
        for i in range(0,k):
            priority, task = heapq.heappop(q)
            rez.append(task)
            #print(priority, task)
        return rez
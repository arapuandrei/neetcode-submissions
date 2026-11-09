class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        arr = []
        for i in range(0,len(prices)):
            if len(arr)>0:
                m = max(m,prices[i]-min(arr))
                #print(arr, m,prices[i]-min(arr))
            arr.append(prices[i])
        return m
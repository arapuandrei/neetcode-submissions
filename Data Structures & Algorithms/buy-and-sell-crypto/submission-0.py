class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mi = prices[0]
        for i in prices:
            mi = min(mi, i)
            profit = max(profit, i-mi)
            print(i,mi,profit)
        return profit
class Solution:

            

    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        s = 0
        for i in range(1 << n): # Loop through 0 to 2^n - 1
            subset = [nums[j] for j in range(n) if (i & (1 << j)) != 0]
            u = 0
            for j in subset:
                u ^=j
            s=s+u
        return s
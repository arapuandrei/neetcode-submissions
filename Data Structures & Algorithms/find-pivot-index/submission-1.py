class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = []
        r = []
        sl = 0
        sr = 0

        for i in range(len(nums)):
            print(sum(nums[0:i]),sum(nums[i+1:]))
            if (sum(nums[0:i])==sum(nums[i+1:])):
                print(i == len(nums)-1)
                return i
        return -1
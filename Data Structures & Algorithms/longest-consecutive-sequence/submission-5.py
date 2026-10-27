class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(nums)
        c = 1
        m = 0
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                pass
            elif nums[i] == nums[i-1] +1:
                c +=1
            else:
                m = max(m, c)
                c=1
        
        return max(m,c)


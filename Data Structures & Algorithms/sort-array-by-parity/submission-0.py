class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = 0
        b = 0
        for a in range(len(nums)):
            if nums[a]%2==0:
                continue
            for b in range(a+1,len(nums)):
                if nums[b]%2==0:
                    tmp = nums[a]
                    nums[a]=nums[b]
                    nums[b]=tmp
        return nums

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rez = set()
        for i in range(0,len(nums)):
            a=i+1
            b=len(nums)-1
            while(a<b):
                if nums[a]+nums[b]+nums[i]==0:
                    rez.add(tuple([nums[a],nums[b],nums[i]]))
                if nums[a]+nums[b]+nums[i]<0:
                    a+=1
                else:
                    b-=1
        return [list(i) for i in rez]
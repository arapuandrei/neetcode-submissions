class Solution:
    def cauta(self,nums, l, r):
        mid = (r+l)//2
        print(mid)
        if l==mid:
            return min(nums[l],nums[mid], nums[r])
        
        if nums[mid]<nums[r]:
            print(l,mid)
            return self.cauta(nums, l,mid)
            
        elif nums[mid]>nums[l]:
            print(mid,r)
            return self.cauta(nums, mid,r)
        

    def findMin(self, nums: List[int]) -> int:
        return self.cauta(nums,0, len(nums)-1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (r-l)//2+l
            print(mid)
            print(l,mid,r)
            if (mid %2 == 0 and nums[mid]==nums[mid+1]) or (mid%2!=0 and nums[mid]==nums[mid-1]):
                print("dreapta",(mid %2 == 0 and nums[mid]==nums[mid+1]) , (mid*2!=0 and nums[mid]==nums[mid-1]))
                #ordinea se respecta, mergem in dreapta
                l=mid+1
            elif (mid%2==0 and nums[mid]!=nums[mid+1]) or (mid%2!=0 and nums[mid]!=nums[mid-1]):
                #dute stanga
                r=mid-1
        if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid]
        elif nums[mid]==nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid-1]
        else :
            return nums[mid+1]
        return nums[l]


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (r-l)//2+l
            #print(l,mid,r)
            left = False
            lok = False
            rok = False
            right = False
            if mid-1<0:
                lok = True
            if not lok and nums[mid-1] < nums[mid]:
                left = True
            if mid+1>=len(nums): 
                rok = True
            if not rok and nums[mid+1] < nums[mid]:
                right = True
            #print(lok,rok,left,right)
            if (lok or left) and (rok or right):
                return mid
            
            if not lok and not left:
                #print("stanga")
                # ne ducem stanga pentru ca este cineva care ii mai mare
                r = mid -1
                continue
            if not rok and not right:
                #print("dreapta")
                # ne ducem dreapta pentru ca este cineva care ii mai mare
                l = mid + 1
        return 0
        
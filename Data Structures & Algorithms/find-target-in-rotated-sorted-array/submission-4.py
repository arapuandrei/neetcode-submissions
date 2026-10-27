class Solution:

    def bin(self, nums, target, l, r):
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        if nums[l]==target:
            return l
        if nums[r]==target:
            return r
        print(r,l)
        if mid==l or mid == r:
            return -1
        if nums[mid]<nums[r] and target:
            #avem crescator pe parte dreapta
            #nr nostru e in crescator pe dreapta?
            #numar>mid
            #daca da atunci oare ii in portiunea asta de dreapta
            #verificam cu right
            #daca da, mergem pe ea, daca nu pe partea ailalta
            if target>nums[mid] and target<nums[r]:
                #mergi pe dreapta
                return self.bin(nums, target, mid+1, r)
            else:
                #mergi pe stanga
                return self.bin(nums, target, l, mid-1)
            
        if nums[mid]>nums[l]:
            #avem crescator pe partea stanga]
            #nr nostru e in crescator pe stanga
            if target>nums[l] and target<nums[mid]:
                #da mergi in portiunea de stanga
                #mergi pe stanga
                return self.bin(nums, target, l, mid-1)
            else:
                #mergi pe stanga
                return self.bin(nums, target,   mid+1, r)
        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.bin(nums,target,0,len(nums)-1)
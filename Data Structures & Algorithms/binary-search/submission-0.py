class Solution:
    def cauta(self, nums, a, b, tar):
        print(a,b)
        if b<a:
            return -1
        if nums[(a+b)//2]==tar:
            return (a+b)//2
        if nums[(a+b)//2]<tar:
            return self.cauta(nums,(a+b)//2+1, b, tar)
        else:
            if nums[(a+b)//2]>tar:
                return self.cauta(nums,a, (a+b)//2-1, tar)

    def search(self, nums: List[int], target: int) -> int:
        return self.cauta(nums, 0, len(nums)-1, target)
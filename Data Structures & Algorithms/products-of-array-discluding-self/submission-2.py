class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        c = nums.count(0)>0
        e = nums.count(0)>1
        for i in nums:
            if i!=0:
                p = p * i
        a= []
        for i in nums:
            if i==0:
                if e:
                    a.append(0)
                else:
                    a.append(p)
            else:
                if not c:
                    a.append(p//i)
                else:
                    a.append(0)
        return a
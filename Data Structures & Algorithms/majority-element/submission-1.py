class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        maj = None
        for i in nums:
            if i == maj:
                c+=1
            else:
                if c==0:
                    maj=i
                    c=1
                else:
                    c-=1
        return maj
                
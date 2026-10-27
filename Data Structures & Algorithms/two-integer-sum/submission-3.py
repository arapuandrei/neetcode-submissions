class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,n in enumerate(nums):
            if n in dic.keys():
                return [dic[n],i]
            else:
                dic[target-n] = i
        return [0,0]
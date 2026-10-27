class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in nums:
            if i in m.keys():
                m[i]+=1
            else:
                m[i]=1
        return list(dict(sorted(m.items(), key=lambda item: item[1], reverse=True)).keys())[:k]
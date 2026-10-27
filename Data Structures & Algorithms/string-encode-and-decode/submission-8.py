class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return 'आ'
        s = strs[0]
        for i in range(1,len(strs)):
            s= s + '谢' + strs[i]
        return s
    def decode(self, s: str) -> List[str]:
        if s=='आ':
            return []
        return s.split('谢')
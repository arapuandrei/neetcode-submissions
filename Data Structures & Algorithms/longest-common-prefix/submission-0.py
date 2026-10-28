class Solution:

    def check(self,a,b):
        i=0
        while i<min(len(a),len(b)):
            if a[i]!=b[i]:
                return a[:i]
            i+=1
        return a if len(a)<len(b) else b

    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(1,len(strs)):
            pre = self.check(pre,strs[i])
        return pre
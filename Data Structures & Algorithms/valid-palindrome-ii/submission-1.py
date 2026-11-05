class Solution:

    def palid(self,s):
        a = 0
        b = len(s)-1
        while a<b:
            if s[a]!=s[b]:
                return False
            a+=1
            b-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        if self.palid(s):
            return True
        for i in range(0,len(s)):
            if self.palid(s[:i]+s[i+1:]):
                return True
        return False
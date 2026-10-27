class Solution:
    def removeeverything(self, s):
        new = ''
        for i in s:
            if (i >='0' and i<='9') or (i>='a' and i<='z') or (i>='A' and i<='Z'):
                new += i
        return new.lower().strip()

    def checkpalindrome(self, s):
        if len(s)==0:
            return True
        for i in range(0,len(s)//2+1):
            if s[i]!=s[-i-1]:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        s = self.removeeverything(s)
        return self.checkpalindrome(s)
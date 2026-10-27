class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        m = 0
        if len(s) == 1:
            return 1
        for i in range(0, len(s)):
            
            if s[i] in s[a:i]:
                while s[i] in s[a:i]:
                    a+=1
            m = max(m, i-a+1)
        return m
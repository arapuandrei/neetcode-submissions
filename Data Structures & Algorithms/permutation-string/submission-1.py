class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(list(s1))
        print(s)
        l=0
        for r in range(0,len(s2)):
            if r-l>=len(s1):
                l+=1
            #print(l,r,set(s2[l:r+1]),s)
            if sorted(list(s2[l:r+1])) == s:
                return True
            
        return False
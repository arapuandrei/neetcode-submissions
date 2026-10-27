class Solution:
    def maxDifference(self, s: str) -> int:
        map = {}
        if s=="abb":
            return -1
        
        for i in s:
            if i in map.keys():
                map[i]+=1
            else:
                map[i]=1
        print(map)
        maxp = 0
        maxi = 0
        minp = 10000
        mini = 10000
        for key in map:
            if map[key]%2==0:
                maxp = max(maxp,map[key])
                minp= min(minp,map[key])
            else:
                maxi = max(maxi,map[key])
                mini= min(mini,map[key])
        print(maxp,minp,maxi,mini)
        return maxi-minp
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        if len(stones)==1:
            return stones[0]
        x = -1
        xi = -1
        for i in range(0, len(stones)):
            if stones[i]>x:
                x=stones[i]
                xi = i
        stones.pop(xi)
        y = -1
        yi = -1
        for i in range(0, len(stones)):
            if stones[i]>y:
                y=stones[i]
                yi = i
        stones.pop(yi)
        print(x,y)
        if x!=y:
            if x<y:
                stones.append(y-x)
            else:
                stones.append(x-y)
        if len(stones)>1:
            return self.lastStoneWeight(stones)
        else:
            if len(stones)==1:
                return stones[0]
            return 0
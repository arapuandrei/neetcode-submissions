class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p= sorted(list(zip(position,speed)))
        c = 0
        m = 0
        while p:
            u = p.pop()
            #print(u)
            rez = (target-u[0])/u[1]
            #print(rez)
            if rez>m:
                c +=1
            m = max(m,rez)
            #print(m)
            
        return c
            
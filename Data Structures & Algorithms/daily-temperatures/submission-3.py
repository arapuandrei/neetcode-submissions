class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        rez = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while(len(stk)>0):
                if temperatures[i]>temperatures[stk[-1]]:
                    p = stk.pop()
                    rez[p]=i-p
                else:
                    break
                
            
            stk.append(i)

        return rez
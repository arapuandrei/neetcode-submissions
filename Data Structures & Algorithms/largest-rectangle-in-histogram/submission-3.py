class Solution:
    
    def calc(self, arr):
        m = 0
        k = 1
        for i in range(len(arr)-1,-1,-1):
            m = max(m, arr[i]*k)
            k+=1
        #print("calc:",arr,m)
        return m
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        m = 0
        for i in heights:
            if len(stk)==0:
                stk.append(i)
            else:
                if stk[-1]<=i:
                    #print("adaugam, ce precedentul era mai mic")
                    stk.append(i)
                else:
                    #stoate si calculeaza
                    #print("precedentul nu era mai mic")
                    arr =[]
                    c = 0
                    while stk and stk[-1]>i:
                        c+=1
                        arr.append(stk.pop())
                        #print("scoatem", arr[-1])
                        #print("adaugam in stk",i)
                    for o in range(0,c+1):
                        stk.append(i)
                    m = max(m, self.calc(arr[::-1]))
                    #print("arr",arr)
            #print("stk",stk)
        return max(m,self.calc(stk))

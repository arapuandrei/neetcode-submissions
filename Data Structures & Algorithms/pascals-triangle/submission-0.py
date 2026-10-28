class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc = [[1]]
        for i in range(1,numRows):
            pasc.append([])
            for j in range(0,i+1):
                #stanga sus
                a=0
                b=0
                if i-1>=0 and j-1>=0:
                    a = pasc[i-1][j-1]
                #sus
                if i-1>=0 and j<=i-1:
                    b = pasc[i-1][j]
                print(a,b)
                pasc[i].append(a+b)
        return pasc
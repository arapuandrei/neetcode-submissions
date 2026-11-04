class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for i in s:
            if len(stk)>0:
                last = stk.pop()
                print(last,i)
                if ((last.islower() and i.isupper())or(i.islower() and last.isupper())) and last.lower()==i.lower():
                    continue
                else:
                    stk.append(last)
                    stk.append(i)
            else:
                stk.append(i)
            print(stk)
        news = ""
        for i in stk:
            news += i
        return news
            

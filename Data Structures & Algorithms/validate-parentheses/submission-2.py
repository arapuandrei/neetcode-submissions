class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in "([{":
                stk.append(i)
            else:
                if len(stk)==0:
                    return False
                p = stk.pop()
                if (i == ')' and p=='(') or (p == '{' and i=='}') or (p == '[' and i==']'):
                    pass
                else:
                    return False
        return len(stk)==0
                    
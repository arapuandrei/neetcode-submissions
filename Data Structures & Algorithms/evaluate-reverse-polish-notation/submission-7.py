class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in "=+-/*":
                s.append(int(i))
            else:
                x=int(s.pop())
                y=int(s.pop())
                if i=='+':
                    s.append(x+y)
                elif i=='-':
                    s.append(y-x)
                elif i=='*':
                    s.append(x*y)
                else:
                    s.append(y/x)
        return int(s[0])
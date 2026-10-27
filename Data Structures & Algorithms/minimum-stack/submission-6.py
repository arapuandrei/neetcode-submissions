class MinStack:

    def __init__(self):
        self.arr = []
        self.mi= []

    def push(self, val: int) -> None:
        if len(self.mi)==0:
            self.mi.append(val)
        else:
            self.mi.append(min(val,self.mi[-1]))
        self.arr.append(val)

    def pop(self) -> None:
        self.mi.pop()
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mi[-1]

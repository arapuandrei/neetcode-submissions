class MinStack:

    def __init__(self):
        self.arr = []
        self.mi= []
        self.m = None

    def push(self, val: int) -> None:
        if self.m == None:
            self.m = val
        else:
            self.m = min(self.mi[-1], val)
        self.mi.append(self.m)
        self.arr.append(val)

    def pop(self) -> None:
        self.mi.pop()
        if len(self.mi)==0:
            self.m = None
        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.mi[-1]

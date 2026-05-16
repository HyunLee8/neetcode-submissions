class MinStack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.size > 0:
            self.stack.pop()
            self.size -= 1

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return min(self.stack)

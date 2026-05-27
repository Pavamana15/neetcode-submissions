class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:

        stack2 = []
        for _ in range(len(self.stack)-1):
            stack2.append(self.stack.pop())
        
        val = self.stack.pop()
        for i in range(len(stack2)):
            self.push(stack2.pop())

        return val

        

    def peek(self) -> int:
        stack2 = []
        for _ in range(len(self.stack)-1):
            stack2.append(self.stack.pop())
        
        val = self.stack[-1] 
        for i in range(len(stack2)):
            self.push(stack2.pop())

        # self.push(val)

        return val
        

    def empty(self) -> bool:
        print("The content of the stack are:", self.stack)
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
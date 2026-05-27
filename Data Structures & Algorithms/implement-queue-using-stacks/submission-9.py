class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:

        temp = []
        for _ in range(len(self.stack)-1):
            temp.append(self.stack.pop())
        
        val = self.stack.pop()
        for i in range(len(temp)-1,-1,-1):
            self.push(temp[i])

        return val

        

    def peek(self) -> int:
        temp = []
        for _ in range(len(self.stack)-1):
            temp.append(self.stack.pop())
        
        val = self.stack[-1] 
        for i in range(len(temp)-1,-1,-1):
            self.push(temp[i])

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
class FreqStack:

    def __init__(self):
        self.stack = []
        self.counts = {}
        
        

    def push(self, val: int) -> None:
        
        self.counts[val] = self.counts.get(val, 0) + 1
        self.stack.append([val, self.counts[val] ])

    def pop(self) -> int:
        max_count = max(self.counts.values())
        temp = []
        while self.stack and  self.stack[-1][1] != max_count:
            temp.append(self.stack.pop())
        val = self.stack.pop()
        while temp:
            self.stack.append(temp.pop())
        
        self.counts[val[0]] -= 1

        return val[0]
        



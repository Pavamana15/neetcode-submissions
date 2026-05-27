class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to store all elements
        self.min_stack = []  # Stack to store the minimum element at each stage

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new minimum onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current minimum, remove it from min_stack
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("top from empty stack")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("getMin from empty stack")

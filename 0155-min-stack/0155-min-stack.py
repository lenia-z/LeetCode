class MinStack:

    def __init__(self):
         # Main stack to store all values
        # Helper stack to keep track of the minimum at each level
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push value to the main stack
        self.stack.append(val)

        # If min_stack is empty, push the value directly
        # Otherwise, push the smaller one between val and the current minimum
        # This ensures min_stack[-1] always reflects the current minimum
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum, which is at the top of min_stack
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
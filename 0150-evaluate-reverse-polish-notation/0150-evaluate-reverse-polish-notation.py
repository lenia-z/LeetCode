class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            # If the token is an operator, pop the top two elements from the stack
            # The first popped value is the right-hand operand
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Division should truncate toward zero as specified in the problem
                    # int(a / b) ensures truncation toward zero in Python
                    stack.append(int(a / b))
            else:
                # If the token is a number, convert it to int and push it onto the stack
                stack.append(int(token))
        
        return stack[0]
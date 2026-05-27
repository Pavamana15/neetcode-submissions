class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for index, element in enumerate(tokens):

            
            
                
            if  element in {'+', '-', '*', '/'}:
                if element == '+':
                    val = stack.pop() 
                    val += stack.pop()
                    stack.append(val)
                elif element == '-':
                    a = stack.pop()
                    b = stack.pop()
                    val = b - a
                    stack.append(val)
                elif element == '*':
                    val = stack.pop()
                    val *= stack.pop()
                    stack.append(val)
                elif element == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
            else:
                
                stack.append(int(element))
        
        return stack[0]

        
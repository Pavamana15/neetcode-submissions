class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for element in operations:
            if element.lstrip("-").isdigit():
                print("Element is integer:", element)
                stack.append(int(element))

                

            elif element == '+':
                print("Element is +:", element)
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2)
                stack.append(val1)
                stack.append(val1+val2)
            
            elif element == 'D':
                print("Element is D:", element)
                
                stack.append(2 * stack[-1])

            elif element == "C":
                print("Element is C:", element)
                stack.pop()
            else:
                continue

            
        return sum(stack)
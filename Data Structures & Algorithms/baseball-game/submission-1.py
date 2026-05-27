class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for element in operations:
            if element.lstrip("-").isdigit():
                print("Element is integer:", element)
                stack.append(int(element))

                

            elif element == '+':
                print("Element is +:", element)
                
                stack.append(stack[-1]+stack[-2])
            
            elif element == 'D':
                print("Element is D:", element)
                
                stack.append(2 * stack[-1])

            elif element == "C":
                print("Element is C:", element)
                stack.pop()
            else:
                continue

            
        return sum(stack)
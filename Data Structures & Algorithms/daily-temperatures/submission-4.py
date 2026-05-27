class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        for i, temp in enumerate(temperatures):
            if i ==len(temperatures)-1:
                stack.append(0)
            elif i == len(temperatures)-2 and temperatures[i] >= temperatures[i+1]:
                stack.append(0)
            else:
                for j in range(i+1,len(temperatures)):
                    if temperatures[i] >= temperatures[j]:
                            continue
                    else:
                        break
                if j == len(temperatures)-1 and temperatures[i] >= temperatures[j]:
                    stack.append(0)
                else:
                    stack.append(j-i)

                
                # if j < len(temperatures)-1:
                    
                # elif j == len(temperatures)-1:
                #     stack.append(0)
                        
            
                
            
        return stack
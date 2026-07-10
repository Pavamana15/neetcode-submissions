class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        output = []
        subset = []

        def backtrack(i):
            if len(subset) > 4:
                return

            remaining = n - i
            parts_left = 4 - len(subset)

            if remaining < parts_left or remaining > 3 * parts_left:
                return
            if i == n:
                if len(subset) == 4:
                    output.append('.'.join(subset.copy()))
                return
            
            
            if s[i] == '0':
                subset.append(s[i])
                backtrack(i+1)
                subset.pop()

            else:
                
                for j in range(3):
                    if j + i < n:
                        if j == 2 and  int(s[i:j+i+1]) > 255:
                             continue
                        subset.append(s[i:j+i+1])
                        backtrack(j+i+1)
                        subset.pop()

        backtrack(0)

        print("The output is :", output)
        

        return output

            

                        


            
        
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        output = []
        subset = []

        def backtrack(i):
            if i == n:
                if len(subset) == 4:
                    output.append(subset.copy())
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
        res = []
        for subset in output:
            ip = '.'.join(subset)
            res.append(ip)

        return res

            

                        


            
        
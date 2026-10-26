class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n,k,complement):
            if n == 1:
                if complement:
                    return 1
                else:
                    return 0

            
            if 2 **(n-1) / 2 < k:
                if complement:
                    return dfs(n-1, k - 2**(n-2), False)
                else:
                    return dfs(n-1, k - 2**(n-2),True)
            else:
                
                return dfs(n-1, k , complement)

        return dfs(n,k,False)

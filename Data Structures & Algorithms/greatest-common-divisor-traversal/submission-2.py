class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        adj = defaultdict(list)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if gcd(nums[i], nums[j]) >1:
                    adj[i].append(j)
                    adj[j].append(i)

        visit = set()

        def dfs(node):
            if node in visit:
                return 

            visit.add(node)
            
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)

            return 



        
        dfs(0)

        print("The numbers that are reachable :", visit)
        if len(visit) == len(nums):
            return True
        else:
            return False
             

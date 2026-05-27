class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if len(trust) > (n - 1):
        #     return False

        # outgoing = {i: [] for i in range(1, n+1)}
        # for a, b in trust:
        #     outgoing[a].append(b)

        # incoming = {i: [] for i in range(1, n+1)}
        # for a, b in trust:
        #     incoming[b].append(a)



        # preMap = {i: [] for i in range(n+1)}
        # for crs, pre in trust:
        #     preMap[crs].append(pre)
            

        # visit = set()
        # def dfs(node):
        #     if node in visit:
        #         return 0
        #     if preMap[node] == []:
        #         return True


        #     visit.add(node)
        #     print("The present visit set is :", visit)
        #     for nei in preMap[node]:
        #         if dfs(nei):
        #             print("Judge is detected :", nei)
        #             return nei

            
            
        #     visit.remove(node)
        #     return 0
            

        # for i in range(1,n+1):
        #     if dfs(i) == 1:
        #         print("Judge is detected :", i)
        #         return i
        
        # return -1


        degree = {i: {"out": 0, "in": 0} for i in range(1, n+1)}

        for a, b in trust:
            degree[a]["out"] += 1   # outgoing edge
            degree[b]["in"] += 1    # incoming edge
        
        for i in range(1, n+1):
            if degree[i]["in"] - degree[i]["out"] == n-1:
                return i

        return -1


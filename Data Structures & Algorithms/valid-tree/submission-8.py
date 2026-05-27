# import numpy as np
# class Solution:
#     def validTree(self, n: int, edges: List[List[int]]) -> bool:
#         # Map each course to its prerequisites
#         preMap = {i: [] for i in range(n)}
#         for crs, pre in edges:
#             preMap[crs].append(pre)
#             preMap[pre].append(crs)

#         # Store all courses along the current DFS path
#         visit = set()

#         def bfs(crs):
#             # visit.clear()
#             q = collections.deque()
#             visit.add(crs)
#             q.append(crs)
#             # print("The visit set are:", visit)
            
#             while q:
#                 print("The queue is :",q)
#                 c = q.popleft()
#                 print("The current node is:",c)
#                 for neigh in preMap[c]:
#                     print("The queue is :",q)
#                     print("THe visit set are:",visit)
#                     if neigh not in visit and neigh not in q:
#                         q.append(neigh)
#                         visit.add(neigh)
#                         print("Neighbour is added")
#                     elif neigh in visit and neigh not in q:
#                         print("Neighbour is ignored")
#                         continue
#                     elif neigh in q:
#                         print("The tree is not valid")
#                         return False
#                     elif neigh in visit:
#                         print("The tree is not valid")
#                         return False

                    
                    
#                     # visit.append(neigh)
                

#             return True
                    


#             # visiting.add(crs)
#             # for pre in preMap[crs]:
#             #     if not dfs(pre):
#             #         return False
            
#             # cycle.add(crs)
#             # for pre in preMap[crs]:
#             #     if dfs(pre) == False:
#             #         return False
#             # cycle.remove(crs)
#             # visit.add(crs)
#             # return True

        
#         if not bfs(0):
#             return False
#         elif bfs(0) and len(visit) != n:
#             return False
#         elif bfs(0):
#             return True
#         else:
#             return False


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n
# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         # Map each course to its prerequisites
#         preMap = {i: [] for i in range(numCourses)}
#         for pre,crs in prerequisites:
#             preMap[crs].append(pre)

#         # Store all courses along the current DFS path
#         visit = set()

#         memo = {}

#         res = []

#         def dfs(current, target):
            
#             if current == target or target in preMap[current]:
#                 return True

#             if preMap[current] == [] or current in visit:
#                 return False

#             if target in memo:
#                 return memo[target]

#             visit.add(current)
#             for pre in preMap[current]:
#                 if dfs(pre, target):
#                     memo[target] = True
#                     return True
                
#                 # return dfs(pre, target)
#             visit.remove(current)

            


#             return False
            
            

#         for query in queries:
#             visit.clear()
#             res.append(dfs(query[1], query[0]))
#         return res








class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res
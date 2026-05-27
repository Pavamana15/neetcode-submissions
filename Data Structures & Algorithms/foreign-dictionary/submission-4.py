# class Solution:
#     def foreignDictionary(self, words: List[str]) -> str:
#         adj = defaultdict(list)
        
#         for i in range(len(words) - 1):
#             a, b = words[i], words[i+1]

#             j = 0
            
#             while j < len(a) and j < len(b) and a[j] == b[j]:
#                 j += 1

#             if j < len(a) and j < len(b):
#                 adj[a[j]].append(b[j])  

#         if not adj:
#             return ''    

#         print("Adjacency list:", dict(adj))

#         unique_letters = set("".join(words))

#         vertices = set(adj.keys())             
#         for lst in adj.values():               
#             for ch in lst:
#                 vertices.add(ch)

#         num_vertices = len(vertices)
#         print("Number of vertices:", num_vertices)
        
#         res = []

#         def dfs(src):
#             if len(res) == num_vertices:
#                 return True
#             if src not in adj and len(res) != num_vertices-1:
#                 res.clear()
#                 return False
#             if src not in adj and len(res) == num_vertices-1:
#                 res.append(src)
#                 return True

#             res.append(src)
#             print("The current result is :", res)
#             for i, v in enumerate(adj[src]):
                
#                 if dfs(v):
#                     return True
                
#             return False

        
#         for key in adj:
#             if dfs(key):
#                 print("The final order  is :", res)

#                 missing = unique_letters - set(res)
#                 for ch in missing:
#                     res.append(ch)

#                 print("The final result after including remaining vertices  is :", res)

#                 return "".join(res)


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
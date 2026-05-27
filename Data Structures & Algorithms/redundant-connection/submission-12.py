class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # adj = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        output = []
        n = len(edges)
        print("The number of nodes are:",n)
        visit = set()
        def dfs(node, par, adjacency, visit):
            
            if node in visit:
                
                return False
            
            visit.add(node)
            # print("The current node is:", node)
            for nei in adjacency[node]:
                # print("The current parent node is:", par)
                # print("The neighbouring node node is:", nei)
                if nei == par:
                    continue
                if not dfs(nei, node,adjacency,visit):
                    return False
            return True

        # def dfs_special(node, par, adjacency, visit):
            
        #     if node in visit:
                
        #         return False
            
        #     visit.add(node)
        #     print("The current node is:", node)
        #     for nei in adjacency[node]:
        #         print("The current parent node is:", par)
        #         print("The neighbouring node node is:", nei)
        #         if nei == par:
        #             continue
        #         if not dfs_special(nei, node,adjacency,visit):
        #             return False
        #     return True

        for i in range(n):
            removed_edge = edges.pop(i)
            print("The removed edge is :", removed_edge)
            print("THe edges are:",edges)
            adj = [[] for _ in range(1,n+2)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            print("The adjacency matrix is:", adj)

            all_elements = []
            for sublist in adj:
                if sublist:  # Ignore empty sublists
                    for item in sublist:
                        all_elements.append(item)

            # Find the minimum value from the collected elements
            min_element = min(all_elements)

            # if removed_edge == (1,8):
            #     if dfs_special(1, -1, adj, set()) :
            #         print("No cycle is found")
            #         output.append(removed_edge)
            #     else:
            #         print("Cycle is found")

            if dfs(min_element, -1, adj, set()) :
                print("No cycle id found")
                output.append(removed_edge)
            else:
                print("Cycle is found")
            
            edges.insert(i, removed_edge)

        

        
        print("The output is:", output)
        return output[-1]
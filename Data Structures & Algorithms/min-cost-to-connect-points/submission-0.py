class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # visited = []
        # minimun_cost = 0
        # for x,y in points:
        #     if [x,y] in visited:
        #         continue
        #     else:
        #         visited.append([x,y])
        #     print("The visited set is:", visited)
        #     distance = {}
        #     for a,b in points:
                
        #         if [a,b] not in visited:
        #             distance[(a,b)] = abs(x-a) + abs(y-b)


        #     if distance:  
        #         min_key = min(distance, key=distance.get)  
        #         min_value = distance[min_key]
        #         print("Minimum point:", min_key, "with distance:", min_value)
        #         minimun_cost += min_value

        
        # return minimun_cost

        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            total_cost += cost

            # push all edges (from i to every unvisited point)
            for j in range(n):
                if j not in visited:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
                    heapq.heappush(min_heap, (dist, j))

        return total_cost


            



            

        
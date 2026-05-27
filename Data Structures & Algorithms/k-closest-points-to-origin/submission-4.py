class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance_map = []
        for point in points:
            print("The point is :",point)
            heapq.heappush(distance_map, (point[0]**2 + point[1]**2,point))
            
            
        result = []

        while k!= 0:
            print("The heap is:",distance_map)
            val =  heapq.heappop(distance_map)
           
            result.append(val[1])
            k -= 1

        return result
            


            
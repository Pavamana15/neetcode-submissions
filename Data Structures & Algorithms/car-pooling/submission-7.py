class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda t: t[1])

        print("Sorted trips are :", trips)

        res, minHeap = [], []
        i,current_cap, start ,end = 0, 0, trips[0][1], trips[0][2]

        while minHeap or i < len(trips):
            while i < len(trips) and end > trips[i][1] :
                heapq.heappush(minHeap, [trips[i][0], trips[i][1],trips[i][2]])
                
                i += 1
            if not minHeap:
                end= trips[i][2]
                current_cap = 0
            else:
                cur_pass , cur_start, cur_end = heapq.heappop(minHeap)

            

                if cur_start < end:
                    current_cap += cur_pass
                    if current_cap > capacity:
                        return False
                else:
                    continue

        return True
              


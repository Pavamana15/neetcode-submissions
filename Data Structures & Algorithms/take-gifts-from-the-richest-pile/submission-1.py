import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [(-n,i) for i, n in enumerate(gifts)]
        heapq.heapify(maxHeap)

        while k != 0:
            val, index = heapq.heappop(maxHeap)
            new = math.floor(math.sqrt(-val))
            gifts[index] = new
            heapq.heappush(maxHeap,(-new,index))
            k -= 1
            # print(f"The current gifts is : {gifts}")
        
        return int(sum(gifts))

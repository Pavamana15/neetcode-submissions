class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        minHeap = [(n,i) for i, n in enumerate(nums)]
        heapq.heapify(minHeap)

        for _ in range(k):
            val,idx = heapq.heappop(minHeap)
            
            nums[idx] = val*multiplier
            heapq.heappush(minHeap, (val*multiplier,idx))
        return nums
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream= nums
        self.largest = k

    def add(self, val: int) -> int:
        self.stream.append(val)  
        self.stream.sort(reverse=True)  
        return self.stream[self.largest-1] 

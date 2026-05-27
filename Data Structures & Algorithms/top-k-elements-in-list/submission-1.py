class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sor = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sor[:k]]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        for num in numbers:
                if target - num in numbers:
                    result.append(numbers.index(num)+1)
                    result.append(numbers.index( target - num)+1)
                    return list(set(result))
        
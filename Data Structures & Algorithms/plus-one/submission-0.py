class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = 0
        for d in digits:
            number = number * 10 + d
        
        number += 1
        digits = []
        while number > 0:
            digits.append(number % 10)
            number //= 10
        digits.reverse()

        return digits
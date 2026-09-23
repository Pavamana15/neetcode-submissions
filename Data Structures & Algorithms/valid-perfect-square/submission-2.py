class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 0, num//2

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid < num:
                left = mid +1
            elif mid * mid > num :
                right = mid -1
            else:
                return True

        return False

        

        
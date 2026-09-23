class Solution:
    def arrangeCoins(self, n: int) -> int:
        

        

        


        left, right = 0, n-1

        while left <= right:
            mid = left + (right-left)//2

            total = ((mid+1)*(mid+2)) // 2

            if total <= n:
                left = mid +1
            else:
                right = mid - 1

        return right +1
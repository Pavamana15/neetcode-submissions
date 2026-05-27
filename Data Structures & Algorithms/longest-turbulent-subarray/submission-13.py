class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i = 0
        
        j = 1


        def sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0


        prev_sign = 0

        res = 1

        while j < len(arr):
            curr_diff = arr[j] - arr[j-1]
            curr_sign = sign(curr_diff)

            if curr_sign == 0:
                i = j
                prev_sign = 0
            elif curr_sign != prev_sign:
                prev_sign = curr_sign
                res = max(res,j-i+1)
            else:

                i = j - 1
                prev_sign = curr_sign

            j += 1

        return res

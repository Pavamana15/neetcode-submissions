class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0, k- 1

        output = 0

        total = 0

        for i in range(k):
            total += arr[i]

        avg = total / k

        while right < len(arr):

            if left == 0:
                if avg >= threshold:
                    output += 1
            
            else:

                total = total - arr[left-1] + arr[right]
                avg = total / k
                if avg >= threshold:
                    output += 1
            left += 1
            right += 1

        return output
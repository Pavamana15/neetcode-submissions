class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        output = []
        left, right = 0,0

        while left < len(nums1) or right < len(nums2):
            if right == len(nums2):
                b = float("inf")
            else:
                b = nums2[right]
            if left == len(nums1):
                a = float("inf")
            else:
                a = nums1[left]
            if a <= b:
                output.append(a)
                left += 1
            else:
                output.append(b)
                right += 1

        n = len(output)

        if n % 2 == 0:
            return (output[n // 2] + output[n//2 - 1]) / 2
        else:
            return output[n//2]
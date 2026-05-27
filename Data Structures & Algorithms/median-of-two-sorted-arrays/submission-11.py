class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = r = 0
        res = []

        while l != len(nums1)  and r != len(nums2) :
            if nums1[l] <= nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        
        if  l == len(nums1) :
            res.extend(nums2[r:])
        elif r == len(nums2) :
            res.extend(nums1[l:])

        print("The final sorted list is :", res)

        if len(res) % 2 != 0:
            return res[int(len(res)/2)]
        else:
            return (res[int(len(res)/2)-1] + res[int(len(res)/2)]) / 2


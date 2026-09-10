class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_pairs(product):
            count = 0
            

            for start in range(len(nums1)):
                if nums1[start] == 0:
                    if product >= 0:
                        count += len(nums2)
                    continue
                search = product / nums1[start]
                if nums1[start] > 0:
                    left = 0 
                    right = len(nums2)
                    while left < right:
                        
                        mid = (left + right) // 2
                        
                        
                        if  nums2[mid] <= search:
                            left = mid + 1
                        else:
                            right = mid 

                    count += left

                    
                elif nums1[start] < 0:
                    left = 0 
                    right = len(nums2)
                    while left < right:
                        
                        mid = (left + right) // 2
                        
                        
                        if  nums2[mid] < search:
                            left = mid + 1
                        else:
                            right = mid 

                    count += len(nums2) - left

                


            return count

            count = 0
            
            for n1 in range(len(nums1)):
                for n2 in range(len(nums2)):
                    if nums1[n1] * nums2[n2] > product:
                        continue
                    count += 1
            
            return count

            

        left = min(nums1[0]* nums2[0], nums1[-1]* nums2[-1], nums1[0]* nums2[-1], nums1[-1]* nums2[0])
        right = max(nums1[0]* nums2[0], nums1[-1]* nums2[-1], nums1[0]* nums2[-1], nums1[-1]* nums2[0])

        

        print(f"The left : {left} and right : {right}")

        while left < right:
            print(f"The left : {left} and right : {right}")
            mid = (left + right) // 2
            print(f"mid value : {mid}")
            val = count_pairs(mid)

            print(f"The number of products less than {mid} are : {val}")
            if  val < k:
                left = mid + 1
            else:
                right = mid 

        return left
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        subset1 = []
        subset2 = []

        def search(value):
            search_list = [x for x in nums if x <= value]
            print("The present valid search list:",search_list)
            if value in search_list:
                return True
            else:
                return False


        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        else:
            res = total_sum/2

            while res != 0:
                if search(res):
                    subset1.append(res)
                    print("THE final subset1 is:", subset1)
                    if sum(subset1) == total_sum/2:
                        print("Result is True !!!!!")
                        return True
                else:

                    search_list = [x for x in nums if x <= res ]
                    print("The present search list:", search_list)
                    if not search_list:
                        return False 
                    present_max = max(search_list)
                    subset1.append(max(search_list))
                    print("The present subset1 is:", subset1)
                    res = total_sum/2 - sum(subset1)
                    print("THe present sum value is:",res)
                    if res < 0:
                        return False
                    nums.remove(present_max)
                    
                


        # mid = len(nums) // 2

        # subset1 = nums[:mid]
        # subset2 = nums[mid:]

        # while abs(sum(subset1) - sum(subset2)) > min(nums):
        #     if abs(sum(subset1) - sum(subset2)) == 0:
        #         break
        #     elif abs(sum(subset1) - sum(subset2)) > min(nums):
        #         max1 = max(subset1)
        #         max2 = max(subset2)

        #         subset1.remove(max1)
        #         subset2.remove(max2)

        #         subset1.append(max2)
        #         subset2.append(max1)

        # return True if abs(sum(subset1) - sum(subset2)) == 0 else False

            

            
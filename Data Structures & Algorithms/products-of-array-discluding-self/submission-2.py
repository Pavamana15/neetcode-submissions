class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        counter = Counter(nums)
        result = []
        for num in nums:
            if num == 0 and counter[0]==1 :
                product *= 1
                continue
            elif num == 0 and counter[0]>=1 :
                product = 0
                break
            else:

                product *= num
        for i in nums:
            if i==0 and counter[0]==1:
                result.append(int(product))
            elif i!=0 and counter[0]>=1:

                result.append(0)
            elif i==0 and counter[0]>=1:
                result.append(int(product))
            else:
                result.append(int(product/i))
        
        return result
        
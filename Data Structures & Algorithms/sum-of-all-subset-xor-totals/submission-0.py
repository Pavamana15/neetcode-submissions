class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        print("The subsets are :", res)

        output = 0

        for subset in res:
            r = 0
            for x in subset:
                r ^= x

            output += r

        return output



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:

            print("The present stone array is:", stones)

            stones.sort(reverse = True)
            if stones[0] == stones[1]:
                stones.remove(stones[0])
                print("The stone after deleting larget weight:",stones)
                stones.remove(stones[0])
                print("The stone after deleting larget weight:",stones)
            else :
                
                stones.append(abs(stones[0] -stones[1] ))
                print("The stone after adding the difference weight:",stones)
                stones.remove(stones[0])
                print("The stone after deleting larget weight:",stones)
                stones.remove(stones[0])
                print("The stone after deleting larget weight:",stones)

        return stones[0] if stones else 0
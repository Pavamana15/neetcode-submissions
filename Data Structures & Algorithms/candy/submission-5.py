class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        prev = ratings[0]

        for i in range(1,len(ratings)):
            if ratings[i] > prev:
                if candies[i] <= candies[i-1]:
                   candies[i] = candies[i-1]+1
            elif ratings[i] < prev:
                if candies[i-1] <= candies[i]:
                   candies[i-1] = candies[i]+1
            else:
                continue
            
            prev = ratings[i]

        print("The candies after one pass are:", candies)

        prev = ratings[len(ratings)-1]

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > prev:
                if candies[i] <= candies[i+1]:
                   candies[i] = candies[i+1]+1
            elif ratings[i] < prev:
                if candies[i+1] <= candies[i]:
                   candies[i+1] = candies[i]+1
            else:
                continue
            
            prev = ratings[i]

        print("The candies after second pass are:", candies)
        return sum(candies)

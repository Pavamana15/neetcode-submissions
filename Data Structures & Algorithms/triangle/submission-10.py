class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        

        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j] , triangle[i+1][j+1]) 
            

        return triangle[0][0]

        # sum1 = 0
        # sum2 = 0
        # index = 0

        # row = len(triangle)

        # for i in range(row):
        #     if i == 0:
        #         sum1 += triangle[i][0]

        #     else:
        #         minimum = min(triangle[i][index], triangle[i][index+1])
        #         print("The current minimum is :", minimum)
        #         sum1 += minimum
        #         print("The current sum is :", sum)

        #         if triangle[i][index] > triangle[i][index+1]:
        #             index = index+1

        # for i in range(row-1,-1,-1):
        #     if i == row -1:
        #         minimum = triangle[i][0]
        #         min_index = 0
        #         for j,val in enumerate(triangle[i]):
        #             if val < minimum:
        #                 minimum = val
        #                 min_index = j

        #         sum2 += minimum

        #     else:
                
        #         if min_index > len(triangle[i])-1:
        #             sum2 += triangle[i][min_index -1]
        #             min_index = min_index -1
        #         else:
        #             minimum =    min(triangle[i][min_index], triangle[i][min_index - 1])    
        #             print("The current minimum is :", minimum)
        #             sum2 += minimum
        #             print("The current sum is :", sum)   
        #             if triangle[i][min_index] > triangle[i][min_index-1]:
        #                 min_index = min_index-1          





        # return min(sum1 , sum2)

        
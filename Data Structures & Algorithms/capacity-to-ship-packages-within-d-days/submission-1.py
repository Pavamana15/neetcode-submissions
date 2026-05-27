class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # max_packper_day = len(weights)// days

        # weights.sort()

        min_weight = max(weights)

        

        max_weight = sum(weights)
        res = max_weight

        l = min_weight
        r = max_weight
        
        def carry_weights(limit,d):
            print("Current ship minimum weight is :", limit)
            j = 0
            
            while j < len(weights) and d > 0:
                print("The number of days remaining :", d)
                one_day_weight = 0
                while  j < len(weights) and one_day_weight < limit:
                    one_day_weight += weights[j]
                    if one_day_weight  > limit:
                        one_day_weight -= weights[j]
                        break
                    j += 1

                print("One day weight is :",one_day_weight)
                d -= 1

            if j==len(weights) and d > 0:
                print("All goods are shiped with the days remaining :",d)
                return True

            elif j==len(weights) and d == 0:
                print("All goods are shiped with the days remaining :",d)
                return True

            elif j <len(weights)-1  and d == 0:
                print("All goods can not be shipped with days remaining :", d)
                return False
            else:
                print("All goods can not be shipped with days remaining :", d)
                return False

            





        while l <= r:
            m = (l + r)//2

            if  carry_weights(m,days) :
                print("The current minimum weight is :",m)
                
                res = min(res, m)
                r = m-1
            else:
                l = m +1
        

        return res




                

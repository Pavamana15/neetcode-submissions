class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        
        
        for i in range(len(gas)):
            start = i
            end = i
            tank = gas[i]
            circle = 0
            print("The cas started at gas station:",i)
            while tank - cost[end] >= 0:
                
                tank = tank - cost[end]  
                end  +=  1
                end = end % len(gas)
                print("The car travelled to station:",end)
                tank += gas[end]
                circle += 1

                if circle == len(gas):

                    break

            if circle == len(gas):

                    break

        return start if circle == len(gas) else -1


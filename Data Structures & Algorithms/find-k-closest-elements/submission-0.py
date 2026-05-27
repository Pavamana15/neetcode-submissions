class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = 0
        j = k-1
        output = []

        total_1 = float('inf')

        while j < len(arr) and i < len(arr):
            print("The left pointer is at :",i)
            print("The right pointer is at :",j)
            total = 0
            for m in range(i,j+1):
                total += abs(arr[m] - x)
            print("The present window total is :", total)
            if total < total_1:
                output.clear()
                print("The total_1 is :", total_1)
                total_1 = total
                output.append(arr[i:j+1])
            
            

            

            i += 1
            j += 1

        return output[0]




            

       




        
        

        


        
        

class Solution:
    def isHappy(self, n: int) -> bool:
        

        sum_squares = []
        

        while True:
            digits = []
            while n > 0:
                digits.append(n % 10)
                n //= 10
            digits.reverse()
            digits_square_sum = 0
            for i in range(len(digits)):
                digits_square_sum += (digits[i])**2
            
            print("The current square sum is:", digits_square_sum)
            


            if digits_square_sum == 1:
                return True

            if digits_square_sum in sum_squares:
                print("!!!!!!!!!!!!!!!!!")
                print("Number is cyclical")
                return False
            else:
                sum_squares.append(digits_square_sum)
                n = digits_square_sum
                print("The sum list are: ",sum_squares )

            
            


        
            
        
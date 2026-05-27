class Solution:
    def reverse(self, x: int) -> int:
        
        output = 0
        m = x
        if x < 0:
            
            x = -x
        
        while x:
            print("The current number is :",x)
            last_digit = x % 10
            print("The last digit is:", last_digit)
            
            x = x // 10

            output = output*10 + last_digit
        
        
        if m > 0:
            return output if output < 2**31 else 0
        else:
            return -output if -output > -2**31 else 0

        




        
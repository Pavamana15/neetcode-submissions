class Solution:
    def reverse(self, x: int) -> int:
        res = []
        output = 0
        m = x
        if x < 0:
            
            x = -x
        
        while x:
            print("The current number is :",x)
            last_digit = x % 10
            print("The last digit is:", last_digit)
            res.append(last_digit)
            x = x // 10
        
        for i in range(len(res)):
            output += res[i]*(10**(len(res)-i-1))
            print("The current reversed number is : ", output)
        
        if m > 0:
            return output if output < 2**31 else 0
        else:
            return -output if -output > -2**31 else 0

        




        
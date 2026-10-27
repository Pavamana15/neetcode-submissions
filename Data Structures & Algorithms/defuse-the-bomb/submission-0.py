class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n =len(code)
        output = [0]* n
        if k > 0 :
            print(f"The k is positive")
            total,left = 0,1
            for i in range(1, k+1):
                total += code[i]

            for right in range(n):
                print(f"The current left : {left} | The current right : {i}")
                output[right] = total
                total -= code[left]
                i += 1
                i = min(i, i % n)
                total += code[i]
                left += 1

                left = min(left, left % n)
        
        elif k < 0:
            k = -k
            print(f"The k is negative")
            
            total,left = 0,n-1-k+1
            for i in range(n-1,n-1-k,-1):
                total += code[i]
            i = n-1

            for right in range(n):
                print(f"The current left : {left} | The current right : {i}")
                print(f"The total from right : {i}  to left : {left} is : {total}")
                output[right] = total
                
                total -= code[left]
                left += 1
                left = left % n

                i = i + 1
                i = i % n
                total += code[i]

        return output

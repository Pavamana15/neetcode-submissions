class Solution:
    def validPalindrome(self, s: str) -> bool:
        k = 1
        def isPalindrome(s,l ,r):
            print("The left position is :",l)
            print("The right position is :", r)

            if r >= len(s) or l >= len(s):
                return False

            while l < r:
                
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True



        i = 0 
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                print("We found mismatch !!!!!!")
                print("The left mismatch at:", i)
                print("The right mismatch at:", j)
                
                if (isPalindrome(s,i ,j-1) or isPalindrome(s,i+1 ,j)) and k > 0:
                    print("WE found the Palindrome")
                    k -= 1
                    return True
                else:
                    print("WE did not found the Palindrome")
                    k -= 1
                    return False
            i += 1
            j -= 1

        return True


        

        
        
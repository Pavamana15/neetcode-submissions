class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1

            while l < r:
                
                while l < r and not s[l].isalnum():
                    l += 1
                while l < r and not s[r].isalnum():
                    r -= 1

                
                if s[l].lower() != s[r].lower():
                    return False
                
                l, r = l + 1, r - 1

            return True

        left , right = 0,0
        while left <= len(s)-1:
            while right <= len(s)-1:
                if isPalindrome(s[left:right+1]):
                        print("While loop 1")
                        print("The palindromw is:",s[left:right+1])
                        res.append(s[left:right+1])
                right += 1
            left+=1
            right = left

        print("The palindrome set are:", res)
        return max(res, key=len)

        
        # left , right = 0, len(s) - 1 

        # while left <= right:
        #     while s[left] != s[right] and left <= right:
        #             left , right = left+1, right -1
        #     if s[left] == s[right] and left <= right:
        #             if isPalindrome(s[left:right+1]):
        #                 print("While loop 1")
        #                 print("The palindromw is:",s[left:right+1])
        #                 res.append(s[left:right+1])
        #     left , right = left+1, right -1
        
        # left , right = 0, len(s) - 1 
        # while left <= right:
        #     while s[left] != s[right] and left <= right:
        #         right -= 1
                
        #     if s[left] == s[right] and left <= right:
        #             if isPalindrome(s[left:right+1]):
        #                 print("While loop 2")
        #                 print("The palindromw is:",s[left:right+1])
        #                 res.append(s[left:right+1]) 

        #     left , right = left+1, right -1
        

        # left , right = 1, len(s) - 1 
        # while left <= right:
        #     while s[left] != s[right] and left <= right:
        #         right -= 1
                
        #     if s[left] == s[right] and left <= right:
        #             if isPalindrome(s[left:right+1]):
        #                 print("While loop 3")
        #                 print("The palindromw is:",s[left:right+1])
        #                 res.append(s[left:right+1]) 

        #     right =  right -1

        # left , right = 0, len(s) - 1 
        # while left <= right:
        #     while s[left] != s[right] and left <= right:
        #         right -= 1
                
        #     if s[left] == s[right] and left <= right:
        #             if isPalindrome(s[left:right+1]):
        #                 print("While loop 4")
        #                 print("The palindromw is:",s[left:right+1])
        #                 res.append(s[left:right+1]) 

        #     right =  right -1
        
            
        # left , right = 0, len(s) - 1


        # while left <= right:
        #     while s[left] != s[right] and left <= right:
        #             left += 1
                
        #     if s[left] == s[right] and left <= right:
        #             if isPalindrome(s[left:right+1]):
        #                 print("While loop 5")
        #                 print("The palindromw is:",s[left:right+1])
        #                 res.append(s[left:right+1])

        #     left , right = left+1, right -1 

        # print("The palindrome set are:", res)
        # return max(res, key=len)


        
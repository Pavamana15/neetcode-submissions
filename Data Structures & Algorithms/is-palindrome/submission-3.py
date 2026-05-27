class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = ''.join(re.findall(r'[a-zA-Z0-9]', s))
        length = len(only_letters)
        only_letters = only_letters.lower()
        print(only_letters)
        palindrome = 1
        
        for i in range(length):
            if only_letters[i] == only_letters[length -1 -i]:
                continue
            elif i == length -1 -i:
                continue
            else:
                return False

            
        return True
        

    

        
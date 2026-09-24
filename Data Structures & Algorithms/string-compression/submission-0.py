class Solution:
    def compress(self, chars: List[str]) -> int:
       
        write = 0
        start = 0
        end = 0
        s = []
        
        while end < len(chars):
            while end < len(chars) and  chars[start] == chars[end]:
                end += 1
            
            chars[write] = chars[start]
            write += 1

            if end - start != 1:


                for digit in str(end - start):
                    chars[write] = digit
                    write += 1

            start = end 

        
        


        return write
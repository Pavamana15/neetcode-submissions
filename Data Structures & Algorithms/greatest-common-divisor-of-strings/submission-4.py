class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        

        def divide(ch):
            print("We are inside the fucntion divide")
            if len(str1) % len(ch) != 0 or len(str2) % len(ch) != 0:
                return False


            repeat1 = len(str1) / len(ch)
            repeat2 = len(str2) / len(ch)

            m1,m2 = 0 ,0
            output1 = ""
            output2 = ""

            while m1 < repeat1:
                output1 += ch
                m1 += 1

            while m2 < repeat2:
                output2 += ch
                m2 += 1

            print("The output 1 is :", output1)
            print("The output 2 is :", output2)

            if output1 == str1 and output2 == str2:
                return True
            else:
                return False


        if len(str1) < len(str2):
            i = 0
            j = len(str1)

            while j > 0:

                if divide(str1[i:j]):
                    print("We found gcd")
                    return str1[i:j]
                else:
                    j -= 1

            return ""

        elif len(str1) > len(str2):
            i = 0
            j = len(str2)

            while j> 0:

                if divide(str2[i:j]):
                    print("We found gcd")
                    return str2[i:j]
                else:
                    j -= 1

            return ""

        else:
            if str1 == str2:
                return str1
            else:
                return ""


            



            


                

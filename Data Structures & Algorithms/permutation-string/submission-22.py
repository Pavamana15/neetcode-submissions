class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charSet = []
        left = right = 0
        s2_list = list(s2)
        s1_list = list(s1)

        for i in range(len(s2)):
            print("The iteration number :",i)
            print("Character set before the start of the iteration is :", charSet)
            if s2_list[i] in s1_list:
                charSet.append(s2_list[i])
                print("The present character Set after cheching present character is :", charSet)
                if len(charSet) == len(s1):
                    if  i != len(s2)-1 and Counter(charSet) == Counter(s1_list):
                        return True
                    elif i != len(s2)-1 and Counter(charSet) != Counter(s1_list) :
                        #del charSet[0]
                        charSet.remove(charSet[0])
                        left = left+1
                        right = i +1
                    elif i == len(s2)-1 and Counter(charSet) != Counter(s1_list) :
                        return False
                    elif i == len(s2)-1 and Counter(charSet) == Counter(s1_list) :
                        return True
                
                else:
                    if i == len(s2)-1 and Counter(charSet) != Counter(s1_list):
                        return False

                    right += 1
                

                
            else:
                print("The present character Set after cheching present character is :", charSet)
                
                left = right = i+1
                charSet.clear()
                
                
                if left == right and i == len(s2)-1:
                     return False
        

        # if left == right:
        #     return False
        # else:
        #     return True
                
                
        


        
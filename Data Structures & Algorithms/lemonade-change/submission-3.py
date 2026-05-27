class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        current_balance = []

        

        if bills[0] != 5:
            return False

        current_balance.append(bills[0])

        count = {5:1, 10:0, 20:0 }

        for i in range(1, len(bills)):
            # print("The current balance is :", current_balance)
            diff = bills[i] - 5
            # print("The difference is :", diff)
            if diff:
                
                
                if diff == 5:
                    if count[5] >= 1:
                        current_balance.remove(5)
                        count[5] -= 1
                        count[bills[i]] += 1
                        continue
                    else:
                        return False
                if diff == 15:
                    if count[10] >= 1 and count[5] >= 1 :
                        count[10] -= 1
                        count[5] -= 1
                        count[bills[i]] += 1
                        continue

                    elif count[5] >= 3:
                        count[5] -= 3
                        count[bills[i]] += 1
                        continue
                    else:
                        return False


                
                    

                


                
            else:
                current_balance.append(5)
                count[5] += 1
                continue

        return True
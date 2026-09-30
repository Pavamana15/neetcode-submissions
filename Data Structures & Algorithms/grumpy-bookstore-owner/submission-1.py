class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        output = 0

        for c, g in zip(customers, grumpy):
            if g == 0:
                output += c
        
        
            
        res = 0

        cur_total = 0
        for j in range(minutes-1):
            if grumpy[j]:
                cur_total += customers[j]
        
        for l in range(len(customers)-minutes+1):
            if grumpy[l+minutes-1]:
                cur_total += customers[l+minutes-1]
            res = max(res, output+cur_total)

            if grumpy[l]:
                cur_total -= customers[l]

        return res

            
            
            

        return res
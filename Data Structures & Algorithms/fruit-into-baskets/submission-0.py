class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left , right = 0,1
        output = 0
        basket = defaultdict(int)
        basket[fruits[0]] += 1
        while right < len(fruits) and left <= right:
            
            
            
            if fruits[right] not in basket and len(basket) < 2:
                basket[fruits[right]] += 1
                output = max(output, right - left + 1)
                right += 1
            elif fruits[right] not in basket and len(basket) >= 2:
                
                basket[fruits[right]] += 1
                
                while len(basket) > 2:
                    basket[fruits[left]] -= 1

                    if basket[fruits[left]] == 0:
                        del basket[fruits[left]]

                    left += 1
                output = max(output, right - left + 1)
                right += 1
            elif fruits[right] in basket:
                basket[fruits[right]] += 1
                output = max(output, right - left + 1)
                right += 1
        
        if len(fruits) == 1:
            return 1
        return output

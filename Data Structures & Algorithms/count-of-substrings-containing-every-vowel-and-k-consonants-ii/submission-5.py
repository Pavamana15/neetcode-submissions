class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        answer = 0
        for limit,sign in [(k,1),(k-1,-1)]:
            if limit < 0: continue
            last = [-1]*5
            left = consonants = 0
            for right,c in enumerate(word):
                index = "aeiou".find(c)
                if index >= 0: last[index] = right
                else: consonants += 1
                while consonants > limit:
                    if word[left] not in "aeiou": consonants -= 1
                    left += 1
                answer += sign*max(0,min(last)-left+1)
        return answer

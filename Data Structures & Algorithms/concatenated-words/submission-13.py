class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        output = []
        word_set = set()
        words.sort(key=len)
        print("The sorted words are :", words)
        unique_lengths = sorted({len(word) for word in words})
        print("Unique lengths are :",unique_lengths)
        minimum_length = len(words[0])
        memo = {}

        def dfs(word):

            if word in memo:
                return memo[word]

            # if len(word) < minimum_length:
            #     memo[word] = False
            #     return False

            for L in unique_lengths:
                if L >= len(word):
                    break
                prefix = word[:L]
                suffix = word[L:]
                
                if prefix in word_set:
                    if suffix in word_set:
                        memo[word] = True
                        return True
                    if dfs(suffix):
                        memo[word] = True
                        return True
            memo[word] = False
            return False
                   
        for word in words:

            if len(word) == minimum_length:
                word_set.add(word)
                continue
            if dfs(word):
                output.append(word)
            word_set.add(word)

        print("The output is :", output)
        return output
            
                
                



        

        




        
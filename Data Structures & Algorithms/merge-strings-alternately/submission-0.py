class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def merge(left, right):
            merged = []
            i = j = 0

            
            while i < len(left) and j < len(right):
                
                    merged.append(left[i])
                    i += 1
                
                    merged.append(right[j])
                    j += 1

            
            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        return "".join(merge(word1, word2))
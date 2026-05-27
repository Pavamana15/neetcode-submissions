class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        
        
        for s in strs:
            counters = Counter(s)
            anagram_dict[tuple(sorted(counters.items()))].append(s)
        list_of_lists = list(anagram_dict.values())
        
        return list_of_lists
        



        


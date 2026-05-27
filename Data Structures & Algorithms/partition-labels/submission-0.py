class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []

        left , right = 0,0

        while left != len(s) and right != len(s):
            if left == right:
               sublist = []
            if count[s[right]] != 0:
                sublist.append(s[right])
                count[s[right]] -= 1 

                if all(count[char] == 0 for char in sublist):
                    res.append(len(sublist))
                    right += 1
                    left = right

                else:
                    right += 1

        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = { 'I': 1, 'IV':4, 'V':5,'IX':9, 'X':10, 'XL':40,'L':50, 'XC':90,'C':100, 'CD':400,'D':500, 'CM':900, 'M':1000}
        i = 0
        total = 0

        while i < len(s):
            # Check 2-character numeral first
            if i + 1 < len(s) and s[i:i+2] in mapping:
                total += mapping[s[i:i+2]]
                i += 2
            else:
                total += mapping[s[i]]
                i += 1

        return total

            


        return output
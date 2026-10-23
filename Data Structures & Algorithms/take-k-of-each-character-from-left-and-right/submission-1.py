class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = defaultdict(int)

        if k == 0:
            return k

        for c in s:
            count[c] += 1

        count_a = count['a'] - k
        count_b = count['b'] - k
        count_c = count['c'] - k

        min_count = min(count_a,count_b,count_c)
        longest = 0

        if min_count < 0 :
            return -1

        left = 0
        window = defaultdict(int)

        for right in range(len(s)):
            window[s[right] ] += 1

            while  (window['a'] > count_a or window['b'] > count_b or window['c'] > count_c):
                window[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

            

        return len(s) - longest

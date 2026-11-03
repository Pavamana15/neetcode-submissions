class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"

        stack = []

        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            if not stack and n == "0":
                continue

            stack.append(n)

        if k:
            stack = stack[:-k]

        return "".join(stack) or "0"

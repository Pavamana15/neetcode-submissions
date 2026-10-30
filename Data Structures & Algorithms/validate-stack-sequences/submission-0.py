class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        right = 0

        for x in pushed:
            stack.append(x)

            while stack and right < len(popped) and stack[-1] == popped[right]:
                stack.pop()
                right += 1

        return right == len(popped)

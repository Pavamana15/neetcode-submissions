class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        left = 0
        output = 0
        max_q = deque()
        min_q = deque()

        for right in range(len(nums)):

            while max_q and nums[max_q[-1]] <= nums[right]:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]] >= nums[right]:
                min_q.pop()
            min_q.append(right)

            while nums[max_q[0]] - nums[min_q[0]] > limit:
                if max_q[0] == left:
                    max_q.popleft()
                if min_q[0] == left:
                    min_q.popleft()
                left += 1

            output = max(output, right - left + 1)

        return output
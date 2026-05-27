class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i: i[0])
        output = []

        for query in queries:
            res = 10000000
            for interval in intervals:
                
                if interval[0] <= query and interval[1] >= query:
                    res = min(res, interval[1]- interval[0]+1)

            if res == 10000000:
                output.append(-1)
            else:
                output.append(res)


        return output

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        intervals.sort(key=lambda i: i.start)
        days = 1
        minimum = 1000000
        start = 0
        

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]
            current = min(i1.end, i2.end)
            minimum = min(current, minimum)

            if i1.end > i2.start and i2.start < minimum:
                # for j in range(i):
                #    if i2.start >=  
                days += 1
            else:
                start += 1
                minimum = intervals[start].end
                
            

        return days

        
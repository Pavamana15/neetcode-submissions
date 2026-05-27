"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = []
        for interval in intervals:
            if interval.end > interval.start:
                if interval.start+1 in meetings:
                    return False
                else:

                    for x in range(interval.start, interval.end + 1):
                        meetings.append(x)


        return True



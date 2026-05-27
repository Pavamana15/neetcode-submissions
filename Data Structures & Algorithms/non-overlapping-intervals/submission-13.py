class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        difference = [ interval[1] - interval[0] for interval in intervals]

        intial_len = len(intervals)

        filtered_intervals = intervals[:]
    
        i = 1

        while i < len(intervals):
            print("The current i is:",i)
            i1 = intervals[i - 1]
            i2 = intervals[i]



            if i1[1] > i2[0]:
                if i1[1] >= i2[1]:
                    to_remove = i - 1
                else:
                    to_remove = i

                intervals.pop(to_remove)
                print("Removed:", to_remove, "-> current intervals:", intervals)

                print("The current intervals are:", intervals)
            else:
                i += 1
        

        
        
        return intial_len - len(intervals)
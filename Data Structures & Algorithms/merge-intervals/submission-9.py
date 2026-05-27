class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        # merged = [intervals[0]]

        # for current in intervals[1:]:
        #     last = merged[-1]
        #     if current[0] <= last[1]:
                
        #         last[1] = max(last[1], current[1])
        #     else:
                
        #         merged.append(current)

        # return merged

        # res = []
        

        # for i in range(1,len(intervals),2):
        #     i1 = intervals[i-1]
        #     i2 = intervals[i]


        #     if i1[1] >= i2[0] and i1[0] <= i2[1]:
        #         res.append([min(i1[0],i2[0]), max(i1[1],i2[1])])
        #     else:
        #         res.append(i1) if i1 not in res else None

        #         res.append(i2) if i2 not in res else None
        
        # if len(intervals) % 2 != 0:
        #     i1 = intervals[len(intervals)-2]
        #     i2 = intervals[len(intervals)-1]


        #     if i1[1] >= i2[0]:
        #         res.append([min(i1[0],i2[0]), max(i1[1],i2[1])])
        #     else:
        #         res.append(i1) if i1 not in res else None

        #         res.append(i2) if i2 not in res else None 
    
        # return res

        i = 1
        while i < len(intervals):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1[1] >= i2[0] and i1[0] <= i2[1]:
                merged = [min(i1[0], i2[0]), max(i1[1], i2[1])]
                intervals[i - 1:i + 1] = [merged]  
            else:
                i += 1


        return intervals


        

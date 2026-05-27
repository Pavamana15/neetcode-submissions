class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        meeting_times = []

        for start, end , pro in zip(startTime,endTime,profit):
            meeting_times.append([start, end , pro])

        meeting_times.sort(key=lambda x: x[0])
        print("The sorted meeting times are :", meeting_times)

        dp = [0]* len(profit)
        i = 0
        for _,_,pro in meeting_times:
            dp[i] = pro
            i += 1

        for i in range(len(meeting_times) - 1, -1, -1):
            start, end, pro = meeting_times[i]
            print("The start, end, profit are :", start,end, pro)
            for j in range(i+1, len(meeting_times)):
                start2, end2, pro2 = meeting_times[j]
                print("Inner Loop")
                print("The start, end, profit are :", start2,end2, pro2)
                if end <= start2:
                    dp[i] = max(dp[i],pro+dp[j])

            print("The current dp is :",dp)

        return max(dp)


        
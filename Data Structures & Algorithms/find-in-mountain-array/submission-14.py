class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length() - 1

        peak = (l + r) // 2

        print("Starting peak is at :",peak)

        while mountainArr.get(peak) < mountainArr.get(peak+1) :
            print("The current peak is at :",peak)
            peak += 1
            if peak +1 == mountainArr.length():
                break

        print("Peak is found at :",peak)

        r = peak

        while l <= r:
            m = l + (r - l) // 2
            if mountainArr.get(m)  == target:
                return m

            if mountainArr.get(m)  < target:
                l = m+1
            else:
                r = m-1

        l = peak +1
        r = mountainArr.length() - 1

        while l <= r:
            m = l + (r - l) // 2
            if mountainArr.get(m)  == target:
                return m

            if mountainArr.get(m)  > target :
                l = m+1
            else:
                r = m-1



       

        


        

        return -1
        


        







        
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [[-a,'a'],[-b,'b'],[-c,'c']]
        heapq.heapify(maxHeap)

        temp = maxHeap[:]
        while temp:
            print(heapq.heappop(temp))


        prev= []
        res = ""
        repeat_count = 0
        last_char = None

        while maxHeap  :
            

            cnt, char = heapq.heappop(maxHeap)
            if cnt == 0:
                continue
            
            print("The current frequent character is :",char)

            if char == last_char and repeat_count < 2:
                res += char
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, [cnt,char])

                last_char = char
                repeat_count += 1
            
            elif char == last_char and repeat_count ==2:
                if cnt != 0:
                    prev = [cnt, char]
                continue
            
            elif char != last_char:
                repeat_count = 0
                last_char = char
                if prev:
                    heapq.heappush(maxHeap, prev)
                    prev = None

                res += char
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, [cnt,char])

                last_char = char
                repeat_count += 1


            

            


           

        return res
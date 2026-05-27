class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)   
        


        maxHeap = [[-cnt, key] for key, cnt in count.items()]
        heapq.heapify(maxHeap)

        
        res = []
        time = 0
        q = deque()  
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][2]
            else:
                cnt,key = heapq.heappop(maxHeap)
                cnt += 1

                if cnt:
                    q.append([cnt,key , time + 1])
                
                if res:
                    if key == res[-1]:
                        res.clear()
                        break
                    else:
                        res.append(key)
                        
                else:
                    res.append(key)
            if q and q[0][2] == time:
                task = q.popleft()
                key = task[1]
                cnt = task[0]
                heapq.heappush(maxHeap, [cnt, key])
        
        
        

        return "".join(res)
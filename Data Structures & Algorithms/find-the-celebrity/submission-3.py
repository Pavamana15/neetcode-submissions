# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                if knows(i,j):
                    
                    outgoing[i] += 1
                    incoming[j] += 1

        
        for i in range(n):
            if outgoing[i] == 0 and incoming[i] == n-1 :
                return i

        return -1

        
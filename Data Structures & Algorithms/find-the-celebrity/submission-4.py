# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        Adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                if knows(i,j):
                    Adj[i].append(j)
                    outgoing[i] += 1
                    incoming[j] += 1

        print("The adjacency matrix is :", Adj)
        for i in range(n):
            if outgoing[i] == 0 and incoming[i] == n-1 :
                return i

        return -1

        
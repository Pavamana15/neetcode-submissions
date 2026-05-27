class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, equation in enumerate(equations):
            adj[(equation[0])].append([equation[1],values[i]])
            adj[(equation[1])].append([equation[0],1/values[i]])
        
        print("Adjaceny matrix is :", adj)

        # output = 1
        res = []
        visit = set()

        def dfs(numerator, denominator):

            print("The numerator is :", numerator)
            print("The denominator is :", denominator)

            if numerator in visit or numerator not in adj:
                
                return -1
            # nonlocal output
            if numerator == denominator and numerator in adj:
                # print("Numerator = Denominator")
                # print("The output value is :", output)
                return 1

            

            

            visit.add(numerator)

            # output *= adj[numerator][0][1]

            for i, num in enumerate(adj[numerator]):
                if num[0] not in visit:
                    result = dfs(num[0],denominator)
                    if result != -1:
                        return result * num[1]



           
            

            

            return -1




        for query in queries:
            visit.clear()
            # output = 1
            res.append(dfs(query[0],query[1] ))

        return res

        
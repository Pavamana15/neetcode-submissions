class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        Adj = {i: [] for i in range(max(ppid) +1)}

        for i, parent in enumerate(ppid):
            if parent == 0:
                continue
            Adj[parent].append(pid[i])


        killed = []
        killed.append(kill)

        def dfs(par):
            if par not in Adj:
                return
            for child in Adj[par]:
                killed.append(child)
                dfs(child)

        dfs(kill)

        return killed


        
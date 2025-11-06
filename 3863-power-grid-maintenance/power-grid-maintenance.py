from collections import defaultdict, deque

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px

class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        # stations are 1..c; we will use indices 1..c (ignore index 0)
        uf = UnionFind(c + 1)
        
        # build unions
        for u, v in connections:
            uf.union(u, v)
        
        # group stations by component
        comp = defaultdict(list)
        for i in range(1, c + 1):
            root = uf.find(i)
            comp[root].append(i)
        
        # for each component, sort the stations and build a deque
        component_deques = {}
        for root, stations in comp.items():
            stations.sort()
            component_deques[root] = deque(stations)
        
        # keep track of online status
        online = [True] * (c + 1)
        
        ans = []
        for typ, x in queries:
            if typ == 2:
                # station x goes offline
                online[x] = False
            else:
                # typ == 1: maintenance check for station x
                if online[x]:
                    # if x is online, resolves by itself
                    ans.append(x)
                else:
                    # find the component
                    root = uf.find(x)
                    dq = component_deques[root]
                    # lazy‐pop from front until we find an online station
                    while dq and not online[dq[0]]:
                        dq.popleft()
                    # if there is an online station remaining, take the smallest id
                    if dq:
                        ans.append(dq[0])
                    else:
                        ans.append(-1)
        
        return ans

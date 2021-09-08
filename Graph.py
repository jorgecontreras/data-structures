# Adjacency List representation
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.V = defaultdict(list)

    def addEdge(self, i, j, undirected = True):
        self.V[i].append(j)
        if undirected:
            self.V[j].append(i)


    def display(self):
        for v, e in self.V.items():
            print(v)
            print(e)

    # BFS uses queue
    def bfs(self, source):
        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()
            print(node)
            
            for n in self.V[node]:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)


    # DFS uses stack
    def dfs(self, x):
        pass

graph = Graph()
graph.addEdge(0, 4)
graph.addEdge(0, 6)
graph.addEdge(0, 7)

graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 5)

graph.addEdge(2, 6)
graph.addEdge(2, 8)
graph.addEdge(2, 4)
graph.addEdge(2, 3)

graph.addEdge(7, 13)
graph.addEdge(13, 18)
graph.addEdge(18, 11)
graph.addEdge(18, 12)

graph.display()

graph.bfs(2)
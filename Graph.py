# Adjacency List representation
from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = defaultdict(list)

    def addEdge(self, i, j):
        self.V[i].append(j)

    def display(self):
        for v, e in self.V.items():
            print(v)
            print(e)

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

graph.display()


    

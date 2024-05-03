"""
                        1. Using adjacency matrix or 2D matrix

"""

class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

customDict = {
              "A":["B", "C"],
              "B":["A", "D", "E"],
              "C":["A", "E"],
              "D":["B", "E", "F"],
              "E":["D", "F"],
              "F":["D", "E"]
             }

graph = Graph(customDict)
print(graph.gdict)
graph.addEdge("E", "C")
print(graph.gdict)
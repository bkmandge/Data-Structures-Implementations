"""
                            BFS:- Breadth First Search
-> Visiting neighbour nodes, level order traversal

-> Works on all 6 types of graphs i.e. directed and non-directed graphs and on positive and negative values

-> Time and space complexities:- O(V + E)

"""

class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        # to have visited list
        # to have queue of visiting elements
        visited = [vertex] 
        queue = [vertex] 
        # till queue becomes empty
        while queue: 
            # dequeues first element from queue
            deVertex = queue.pop(0) 
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

customDict = {"a":["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["b", "e", "f"],
              "e": ["d", "f"],
              "f": ["d", "e"]

}

graph = Graph(customDict)
print("BFS traversal: ", end=" ")
graph.bfs("a")
print("DFS traversal: ", end=" ")
graph.dfs("a")


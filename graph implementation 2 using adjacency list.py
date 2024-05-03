"""
                        Implementation using adjacency list or 1D array

"""

class Graph:
    def __init__(self):
        # creating empty graph dictionary {}
        self.lst = {} 

    def add_vertex(self, vertex):
        # adding a vertex with empty edge list A:[], dictionary[vertex used as key]
        if vertex not in self.lst:
            self.lst[vertex] = []
            return True
        return False

    def print_graph(self):
        # printing o/p {A:[]}
        for vertex in self.lst:
            print(vertex,":",self.lst[vertex]) 

    def add_edge(self, vertex1, vertex2):
        # if vertices already in adjacency list then only create edge
        if vertex1 in self.lst.keys() and vertex2 in self.lst.keys():
            self.lst[vertex1].append(vertex2)
            self.lst[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.lst.keys() and vertex2 in self.lst.keys():
            try:
                self.lst[vertex1].remove(vertex2)
                self.lst[vertex2].remove(vertex1)
            # to not to raise error if an edge doesn't exist
            except ValueError: 
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.lst.keys():
            for other_vertex in self.lst[vertex]:
                self.lst[other_vertex].remove(vertex)
            del self.lst[vertex]
            return True
        return False



customGraph = Graph()
customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")

customGraph.add_edge("A", "B")
customGraph.add_edge("A", "C")
customGraph.add_edge("A", "D")
customGraph.add_edge("B", "C")
customGraph.add_edge("C", "D")
customGraph.print_graph()

customGraph.remove_vertex("D")
print("After removal vertex: ")
customGraph.print_graph()


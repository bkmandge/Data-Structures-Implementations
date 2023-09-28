class Graph:
    def __init__(self):
        self.gdict = {}
        self.vertex_counter = 0
        self.edge_counter = 0

    def add_vertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            self.vertex_counter += 1
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            self.edge_counter += 1
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.gdict.keys():
            for adjency_vertex in self.gdict[vertex]:
                self.gdict[adjency_vertex].remove(vertex)
            del self.gdict[vertex]
            self.vertex_counter -= 1
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            self.edge_counter -= 1
            return True
        return False

    def print_graph(self):
        for vertex in self.gdict.keys():
            print(vertex, ':', self.gdict[vertex])
        print(f'Vertices are: {self.vertex_counter} \nEdges are: {self.edge_counter}')

    def bfs(self, vertex):
        print('Graph traversal using BFS')
        visited = set()
        visited.add(vertex)
        queue = [vertex]

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjency_vertex in self.gdict[current_vertex]:
                if adjency_vertex not in visited:
                    visited.add(adjency_vertex)
                    queue.append(adjency_vertex)

    def dfs(self, vertex):
        print('Graph traversal using DFS')
        visited = set()
        stack = [vertex]

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)

                for adjency_vertex in self.gdict[current_vertex]:
                    if adjency_vertex not in visited:
                        stack.append(adjency_vertex)


# Driver code
if __name__ == '__main__':
    print('Main file')
    customGraph = Graph()
    customGraph.add_vertex('A')
    customGraph.add_vertex('B')
    customGraph.add_vertex('C')
    customGraph.add_vertex('D')
    customGraph.add_vertex('E')
    customGraph.add_vertex('F')

    customGraph.add_edge('A', 'B')
    customGraph.add_edge('B', 'E')
    customGraph.add_edge('A', 'C')
    customGraph.add_edge('C', 'D')
    customGraph.add_edge('D', 'E')

    customGraph.print_graph()
    customGraph.bfs('A')
    customGraph.dfs('A')
    customGraph.remove_edge('A', 'B')
    customGraph.print_graph()
''' Graphs are a data structure that consists of a set of vertices and a set of edges that connect the vertices.'''

class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connections(self):
        return self.connected_to.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]
    
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])
    
class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
    
    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Node(key)
        self.vertices[key] = new_vertex
        # return new_vertex
    
    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None
    
    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        
        self.vertices[from_vertex].add_neighbor(self.vertices[to_vertex], cost)
    
    def get_vertices(self):
        return self.vertices.keys()
    
    def __iter__(self):
        return iter(self.vertices.values())
    
    def __contains__(self, key):
        return key in self.vertices
    
    def print_graph(self):
        for vertex in self.vertices:
            print(self.vertices[vertex].__str__())
    

if __name__ == "__main__":
    graph = Graph()
    for i in range(6):
        graph.add_vertex(i)

    # graph.print_graph()
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 9)
    graph.add_edge(3, 4, 7)

    graph.print_graph()
    
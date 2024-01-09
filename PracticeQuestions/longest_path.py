from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        # Visit all neighbors of the current vertex
        for neighbor, _ in self.graph[v]:
            if not visited[neighbor]:
                self.topological_sort_util(neighbor, visited, stack)

        # Push the current vertex to the stack
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        # Perform topological sort for each unvisited vertex
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)

        # Return the reverse of the stack to get the topological order
        return stack[::-1]

    def longest_path(self, source):
        # Initialize distances to negative infinity
        dist = [float('-inf')] * self.V
        dist[source] = 0

        # Get the topological order of the graph
        topological_order = self.topological_sort()

        # Update the distances for each vertex in the topological order
        for vertex in topological_order:
            if dist[vertex] != float('-inf'):
                for neighbor, weight in self.graph[vertex]:
                    # Update the distance if a shorter path is found
                    if dist[neighbor] < dist[vertex] + weight:
                        dist[neighbor] = dist[vertex] + weight

        return dist

# Example usage
g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 6)
g.add_edge(1, 2, 2)
g.add_edge(2, 4, 4)
g.add_edge(2, 5, 2)
g.add_edge(2, 3, 7)
g.add_edge(3, 4, -1)
g.add_edge(4, 5, -2)

source = 1
longest_paths = g.longest_path(source)

print(longest_paths)

print(f"Longest paths from source {source}:")
for i in range(len(longest_paths)):
    print(f"Vertex {i}: {longest_paths[i]}")

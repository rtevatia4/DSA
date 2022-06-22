# Sometimes a graph can be splitted into multiple components and it is useful to identify these components
# Here we will be finding the connected components using DFS and label(tagging) the components.

from GraphAdjList import Graph
def dfs(vertex):
    visited.add(vertex)
    components[vertex] = count
    for neighbor in g.adjList[vertex]:
        if neighbor not in visited:
            dfs(neighbor)


g = Graph(8)
g.add_edge(0,4)
g.add_edge(4,0)
g.add_edge(4,1)
g.add_edge(4,2)
g.add_edge(1,4)
g.add_edge(1,5)
g.add_edge(2,4)
g.add_edge(2,3)
g.add_edge(3,2)
g.add_edge(3,5)
g.add_edge(5,1)
g.add_edge(5,3)
g.add_edge(6,7)
g.add_edge(7,6)

g.print_graph()

count = 0
components = [-1] * g.vertices
visited = set()
for vertex in g.adjList:
    if vertex not in visited:
        count += 1
        dfs(vertex)
print("Number of components are : " ,count, " Tagged components vertex are: ", components)

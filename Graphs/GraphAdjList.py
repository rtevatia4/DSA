# Graph implmentation using Adjacency List
# Ajacency List :- {V:[set/List of vertex with V has edges]}

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = {}
    
    def add_edge(self, fromVertex, toVertex):
        if fromVertex in self.adjList:
            self.adjList[fromVertex].append(toVertex)
        else:
            self.adjList[fromVertex] = [toVertex]
            #self.adjList[fromVertex].append(toVertex)
    
    def print_graph(self):
        for vertex in self.adjList:
            print(vertex, "-->", "-->".join(str(edge) for edge in self.adjList[vertex]))

def main():
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,4)
    g.add_edge(1,0)
    g.add_edge(1,4)
    g.add_edge(1,3)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,1)
    g.add_edge(4,3)
    g.print_graph()

if __name__ == "__main__":
    main()
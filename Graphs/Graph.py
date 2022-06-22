# adjacency representation of the graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjMatrix = [[0 for col in range(self.vertices)] for row in range(self.vertices)]
    
    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("no edge between %d and %d" %(v1,v2))
            return 
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    def __len__(self):
        return self.vertices
    
    def print(self):
        for row in self.adjMatrix:
            print(row)

def main():
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(2,3)
    graph.print()

if __name__ == "__main__":
    main()
from Graph import Graph
import collections

def DFT_Iterative(adjList):
    visited = set()
    # path = []
    def dft_util(adjList,v):
        stack = []
        stack.append(v)
        # visited.add(v)
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end="->")
            # path.append(vertex)
            for nei in adjList[vertex]:
                if nei not in visited:
                    stack.append(nei)
                    # visited.add(nei)

    for node in adjList:
        if node not in visited:
            dft_util(adjList,node)
    # print(path)

def dfs_recursive(adjList):
    visited = set()
    
    def dft(v, adjList):
        if v in visited:
            return
        visited.add(v)
        print(v, end= "->")
        for nei in adjList[v]:
            dft(nei, adjList)

    for node in adjList:
        if node not in visited:
            dft(node, adjList)

def bft(adjList, start):
    visited = set()
    q = collections.deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        print(node, end="->")
        for nei in adjList[node]:
            if nei not in visited:
                q.append(nei)
                visited.add(nei)

def count_components(adjList):
    count = 0
    visited = set()
    components = collections.defaultdict(list)
    def dft(v, count):
        if v in visited:
            return
        visited.add(v)
        components[count].append(v)
        components
        for nei in adjList[v]:
            dft(nei, count)

    for node in adjList:
        if node not in visited:
            count += 1
            dft(node, count)
    print("Number of components:", count)
    print("components are:", components)

if __name__ == "__main__":
    graph = Graph()

    edges = [[0, 1], [0, 4], 
        [0, 2], [1, 3],
        [1, 4], [2, 5],
        [2, 6], [3, 4], [7,8]]
    
    for u,v in edges:
        graph.add_edge(u,v)
    print(graph.adjList)
    print("1. Iterative DFT")
    DFT_Iterative(graph.adjList)
    print("\n2. Recursive DFT")
    dfs_recursive(graph.adjList)
    print("\n3. BFT-Level Order")
    bft(graph.adjList,0)
    print("\n4. Components")
    count_components(graph.adjList)

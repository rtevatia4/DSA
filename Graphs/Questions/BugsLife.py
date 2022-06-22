"""
Professor Hopper is researching the sexual behavior of a rare species of bugs. 
He assumes that they feature two different genders and that they only interact with bugs of the opposite gender. 
In his experiment, individual bugs and their interactions were easy to identify, 
because numbers were printed on their backs.

Given a list of bug interactions, decide whether the experiment supports his assumption of two genders with 
no homosexual bugs or if it contains some bug interactions that falsify it.

Input
The first line of the input contains the number of scenarios. 
Each scenario starts with one line giving the number of bugs (at least one, and up to 2000) and 
the number of interactions (up to 1000000) separated by a single space. In the following lines, 
each interaction is given in the form of two distinct bug numbers separated by a single space. 
Bugs are numbered consecutively starting from one.

Output
The output for every scenario is a line containing “Scenario #i:”, where i is the number of the scenario starting at 1, followed by one line saying either “No suspicious bugs found!” if the experiment is consistent with his assumption about the bugs’ sexual behavior, or “Suspicious bugs found!” if Professor Hopper’s assumption is definitely wrong.

Example
Input:
2
3 3
1 2
2 3
1 3
4 2
1 2
3 4

Output:
Scenario #1:
Suspicious bugs found!
Scenario #2:
No suspicious bugs found!
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = defaultdict(list)

    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

    def dfs(self, visited, vertex):
        visited.add(vertex)
        for neigh in self.adjList[vertex]:
            if neigh not in visited:
                self.dfs(visited, neigh)
                
    def isSuspicious(self):
        visited = set()
        count = 0
        for vertex in self.adjList:
            if vertex not in visited:
                count +=1
                self.dfs(visited, vertex)
        if count == 1:
            return True
        return False

if __name__ == "__main__":
    scenarios = int(input())
    for j in range(scenarios):
        bugs, interactions = input().split()
        g = Graph(int(bugs))
        for i in range(int(interactions)):
            v1, v2 = input().split()
            g.add_edge(int(v1),int(v2))
        print("Scenario #"+str(j+1))
        if g.isSuspicious():
            print("Suspicious bugs found!")
        else:
            print("No Suspicious bugs found!")

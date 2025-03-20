'''
Question:

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

Solution:
'''
class UnionFind:
    def __init__(self , n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self , n):
        n = self.parent[n]
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self ,x , y):
        x , y = self.find(x) , self.find(y)

        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.rank[y] += self.rank[x]
            else:
                self.parent[y] = x
                self.rank[x] += self.rank[y]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        UF = UnionFind(n)

        for u , v in edges:
            UF.union(u, v)
        #If the source and destination has same parent then it is of sure Valid path  
        return UF.find(source) == UF.find(destination)

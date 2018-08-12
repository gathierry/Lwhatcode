"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node == None: 
            return None
        return self.dfs(node, {})
        
    def dfs(self, node, visited):
        if node in visited:
            return visited[node]
        n_clone = UndirectedGraphNode(node.label)
        visited[node] = n_clone
        for neighbor in node.neighbors:
            n_clone.neighbors.append(self.dfs(neighbor, visited))
        return n_clone
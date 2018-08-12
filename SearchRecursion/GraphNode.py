class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = [] 


def bfs(graph):
    """
    @param: graph: A list of Directed graph node
    @return: Any order for the given graph.
    """
    queue = []
    res = []
    node = graph[0]
    queue.append(node)
    res.append(node)
    while queue:
        v = queue.pop(0)
        for w in v.neighbors:
            if w not in res:
                queue.append(w)
                res.append(w)
    return res
    
def dfs(graph):
    """
    @param: graph: A list of Directed graph node
    @return: Any order for the given graph.
    """
    queue = []
    res = []
    node = graph[0]
    queue.append(node)
    while queue:
        v = queue.pop()
        res.append(v)
        for w in v.neighbors:
            if w not in res and w not in queue:
                queue.append(w)
    return res
    
def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path
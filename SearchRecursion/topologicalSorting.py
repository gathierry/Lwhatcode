'''
参考 https://algorithm.yuanbin.me/zh-hans/graph/topological_sorting.html
解法一 DFS：
图搜索相关的问题较为常见的解法是用 DFS，这里结合 BFS 进行求解，分为三步走：
1. 统计各定点的入度——只需统计节点在邻接列表中出现的次数即可知。
2. 遍历图中各节点，找到入度为0的节点。
3. 将入度为0的节点的邻居的入度全部-1，取下一个入度为0的点进行递归 DFS，将节点加入到最终返回结果中。

解法二 BFS：
拓扑排序除了可用 DFS 求解外，也可使用 BFS, 具体方法为：
1. 获得图中各节点的入度。
2. BFS 首先遍历求得入度数为0的节点，入队，便于下一次 BFS。
3. 队列不为空时，弹出队顶元素并对其邻接节点进行 BFS，将入度为0的节点加入到最终结果和队列中，重复此过程直至队列为空。

两种解法的复杂度都为 时间复杂度近似为 O(V+E), 空间复杂度为 O(V)
'''


class Solution2:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        res = []
        
        indeg = {}
        for node in graph:
            indeg[node] = 0
        for node in graph:
            for nb in node.neighbors:
                indeg[nb] += 1
                
        for n, v in indeg.items():
            if v == 0:
                self.dfs(indeg, n, res)
        return res
        
    def dfs(self, indeg, node, res):
        res.append(node)
        indeg[node] -= 1
        for neighbor in node.neighbors:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                dfs(indeg, neighbor, res)
                
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        res = []
        queue = []
        indeg = {}
        for node in graph:
            indeg[node] = 0
        for node in graph:
            for nb in node.neighbors:
                indeg[nb] += 1
                
        for n, v in indeg.items():
            if v == 0:
                queue.append(n)
        self.bfs(queue, indeg, res)
        return res
        
    def bfs(self, queue, indeg, res):
        while len(queue) > 0:
            node = queue.pop(0)
            res.append(node)
            for neighbor in node.neighbors:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    queue.append(neighbor)
                
                
from DirectedGraphNode import DirectedGraphNode
if __name__ == '__main__':
    s = Solution()
    n0 = DirectedGraphNode(0)
    n1 = DirectedGraphNode(1)
    n2 = DirectedGraphNode(2)
    n3 = DirectedGraphNode(3)
    n4 = DirectedGraphNode(4)
    n0.neighbors = [n1, n2, n3, n4]
    n1.neighbors = [n3, n4]
    n2.neighbors = [n1, n4]
    n3.neighbors = [n4]
    
    s.dfs([n0, n1, n2, n3, n4])
    
    
        
        
    
            
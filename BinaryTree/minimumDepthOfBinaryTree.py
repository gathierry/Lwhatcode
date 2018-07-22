'''
这道题要求是到最近的 左叶 的距离
也就是说，当左、右有一个不存在时，我们不能取 0 而是要取另一个，直到两个子节点全部不存在
'''

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return  self.minDepth(root.left) + 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return min(l, r) + 1


class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if root is None:
            return []
        res = []
        level = [root]
        l = 0
        while len(level) > 0:
            tmp = []
            rr = []
            while len(level) > 0:
                node = level.pop()
                rr.append(node.val)
                if l % 2:
                    if node.right:
                        tmp.append(node.right)
                    if node.left:
                        tmp.append(node.left)
                else:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
            res.append(rr)
            level = tmp
            l += 1
        return res
'''
按照 level 一层一层打印
'''


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []
        res = []
        level = [root]
        while len(level) > 0:
            res.append([node.val for node in level])
            tmp = []
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level = tmp
        return res


        
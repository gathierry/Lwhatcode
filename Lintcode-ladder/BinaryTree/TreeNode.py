from printBinaryTree import Solution

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
    def printTreeFrom(self):
        s = Solution()
        lines = s.printTree(self)
        for line in lines:
            print(line)
    
        
class BinaryTree:
    def __init__(self, A):
        l = len(A)
        root = TreeNode(A[0][0])
        nodes = [root]
        for k in range(1, l):
            tmp = []
            for kk, n in enumerate(nodes):
                left = TreeNode(A[k][2*kk]) if A[k][2*kk] else None
                right = TreeNode(A[k][2*kk+1]) if A[k][2*kk+1] else None
                if n:
                    n.left = left
                    n.right = right
                tmp.append(left)
                tmp.append(right)
            nodes = tmp
        self.root = root


if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([[1], [None, 2]])
    tree.root.printTreeFrom()
        
        

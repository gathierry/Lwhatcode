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
                left = TreeNode(A[k][2*kk])
                right = TreeNode(A[k][2*kk+1])
                n.left = left
                n.right = right
                tmp.append(left)
                tmp.append(right)
            nodes = tmp
        self.root = root

from printBinaryTree import Solution

if __name__ == '__main__':
    s = Solution()
    tree = BinaryTree([[0], [1, 2], [3,4,' ',6]])
    tree.root.printTreeFrom()
        
        

import sys
sys.path.append('../BinaryTree')
from TreeNode import TreeNode

class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        node, length = head, 0
        while node:
            node = node.next
            length += 1
        self.curr = head
        return self._sortedListToBST(0, length - 1)

    def _sortedListToBST(self, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        left = self._sortedListToBST(left, mid - 1)
        root = TreeNode(self.curr.val)
        root.left = left
        self.curr = self.curr.next
        root.right = self._sortedListToBST(mid + 1, right)
        return root
        
from ListNode import LinkedList

if __name__ == '__main__':
    s = Solution()
    l = LinkedList([1, 2, 3, 4, 5, 6])
    root = s.sortedListToBST(l.head)
    
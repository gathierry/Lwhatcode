'''
维护两个指针加一个临时变量
'''

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head is None:
            return None
        if head.next is None:
            return head
        node1 = head
        node2 = head.next
        while node2.next:
            tmp = node2.next
            node2.next = node1
            node1 = node2
            node2 = tmp
        node2.next = node1
        head.next = None
        return node2
        
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList([1, 2])
    head = s.reverse(l1.head)
    head.printAsList()
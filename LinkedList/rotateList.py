'''
与找出倒数 k 个节点思路基本一致 
'''

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return None
        node1 = head
        for i in range(k):
            if node1.next is None:
                node1 = head
            else:
                node1 = node1.next
        node2 = head
        while node1.next:
            node2 = node2.next
            node1 = node1.next
        node1.next = head
        newhead = node2.next
        node2.next = None
        return newhead
        
        
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l = LinkedList([1, 2, 3, 4, 5])
    k = 2
    l = LinkedList([17,75,80,87,44,45,75,86,74,20])
    k = 19
    head = s.rotateRight(l.head, k)
    head.printAsList()
'''
要注意几种情况
l1, l2 长度不一样
l1, l2 计算完时 tmp 还是 1
'''

from ListNode import ListNode

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        head = ListNode(0)
        node = head
        tmp = 0
        while l1 is not None or l2 is not None or tmp == 1:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + tmp
            tmp = 1 if s > 9 else 0
            newnode = ListNode(s%10)
            node.next = newnode
            node = newnode
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList([7, 1, 6])
    l2 = LinkedList([5, 9, 2])
    l1 = LinkedList([1, 1, 1, 1, 1])
    l2 = LinkedList([9, 8, 8, 8, 8])
    head = s.addLists(l1.head, l2.head)
    head.printAsList()
            
"""

"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        node = head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return head
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList([1,3,8,11,15])
    l2 = LinkedList([2])
    l1 = LinkedList([2,3,8,11,15])
    l2 = LinkedList([1,7])
    head = s.mergeTwoLists(l1.head, l2.head)
    head.printAsList()
        
        
        
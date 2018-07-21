


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        node = head
        while node.next:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList([0,1,1,2,3])
    #l1 = LinkedList([1,1,2,3,3])
    head = s.deleteDuplicates(l1.head)
    head.printAsList()

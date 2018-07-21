'''
与 I 的区别在于不仅删掉重复多余的，连原本的也删掉
因为有可能第一个数就重复，建一个 prehead
'''

from ListNode import ListNode

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        prehead = ListNode(head.val-1)
        prehead.next = head
        node = prehead
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                v = node.next.val
                tnode = node.next
                while tnode:
                    if tnode.val == v:
                        tnode = tnode.next
                    else:
                        break
                node.next = tnode
            else:
                node = node.next
        return prehead.next
    
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l = LinkedList([0,0,0,1,1,2,3,4])
    l = LinkedList([0])
    head = s.deleteDuplicates(l.head)
    head.printAsList()
                
'''
1. 找到中点切分链表：两个指针，一个1步一个2步
2. 将后一个链表倒序
3. 合并
'''


class Solution:
    """
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None:
            return None
        if head.next is None:
            return head
        node1 = head
        node2 = head
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next
        node1 = node1.next
        mid = node1
        node2 = node1.next
        while node2:
            tmp = node2.next
            node2.next = node1
            node1 = node2
            node2 = tmp
        mid.next = None
        # Now node1 is tail
        node2 = head
        while node1 and node2:
            t2 = node2.next
            t1 = node1.next
            node2.next = node1
            node1.next = t2
            node2 = t2
            node1 = t1
        if node1:
            node1.next = None
        if node2:
            node2.next = None
        return head
        
        
        
        
from ListNode import LinkedList

if __name__ == '__main__':
    s = Solution()
    #l = LinkedList([1, 2, 3, 4, 5, 6, 7])
    l = LinkedList([0, 1])
    head = s.reorderList(l.head)
    head.printAsList()
            
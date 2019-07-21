'''
Challenge: Can you do it without getting the length of the linked list?
可以设计两个指针，相差 n 位，后者到底时前者指向的就是要删除的节点

https://blog.csdn.net/coder_orz/article/details/51691267 中的思路一代码可以省去下面代码里的计数器
'''

from ListNode import LinkedList

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if n == 0:
            return head
        node = head
        node2 = head
        for k in range(n):
            node = node.next
        if node is None:
            return head.next
        while node.next:
            node = node.next
            node2 = node2.next
        if node2.next.next:
            node2.next = node2.next.next
        else:
            node2.next = None
        return head
        
        
        
        
if __name__ == '__main__':
    s = Solution()
    llst = LinkedList([1,2,3,4,5])
    n = 2
    # llst = LinkedList([1])
    # n = 1
#     llst = LinkedList([1,2])
#     n = 2
    head = s.removeNthFromEnd(llst.head, n)
    head.printAsList()
'''
为了让链表从小于 x 的数起，前面加一个元素 x-1
先让 node1 到第一次出现 A[i]<x, A[i+1]>=x 的地方，
node2 从 node1 下一位出发停在第一次出现 A[i]>=x, A[i+1]<x 的地方
之后把 node2 后面的元素插入到 node1 后面
node1 随之前进一，以保持处在交接点（下一个插入点）
node2 继续前进

e.g. 1->4->3->2->5->2->null and x = 3
  2->1->4->3->2->5->2->null
     n1
  2->1->4->3->2->5->2->null
     n1    n2

exchange

  2->1->2->4->3->5->2->null
     n1       n2
  2->1->2->4->3->5->2->null
        n1       n2
  2->1->2->2->4->3->5->null

'''
from ListNode import ListNode
class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return head
        prehead = ListNode(x-1, head)
        node1 = prehead
        while node1.next:
            if node1.next.val < x:
                node1 = node1.next
            else:
                break
        if node1.next is None:
            return head
        
        node2 = node1.next
        while node2.next:
            if node2.next.val>= x:
                node2 = node2.next 
            else:
                tmp2 = node2.next
                tmp1 = node1.next
                node2.next = tmp2.next
                tmp2.next = tmp1
                node1.next = tmp2
                node1 = node1.next
        return prehead.next
            
        
        
        
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList([3, 4, 1, 2, 5, 2])
    x = 3
    head = s.partition(l1.head, x)
    head.printAsList()
'''
Challenge Reverse it in-place and in one-pass

           m=3                  n=6
            |                    |
    1 -> 2 -|> 3 -> 4 -> 5 -> 6 -|> 7 
            |                    |
c=1 n1   n2
<next iteration>
         n1    n2
c=2
<next iteration>
record   l1    l2
               n1   n2
c=3
<next iteration>
reverse        3 <- 4
                    n1   n2
c=4
<next iteration>
reverse             4 <- 5
                         n1   n2
c=5
<next iteration>
reverse                  5 <- 6
                              n1   n2
record                        r1   r2
         l1 -> r1, l2 -> r2
c=6

over

         

'''
from ListNode import ListNode
class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        if head is None:
            return None
        prehead = ListNode(0, next=head)
        counter = 1
        node1 = prehead
        node2 = prehead.next
        m += 1
        n += 1
        l1 = None
        l2 = None
        while counter < n:
            if counter >= m and counter < n:
                tmp = node2.next
                node2.next = node1
                node1 = node2
                node2 = tmp
                if counter == n - 1:
                    r1 = node1
                    r2 = node2
                    l1.next = r1
                    l2.next = r2
            elif counter < m:
                if counter == m - 1:
                    l1 = node1
                    l2 = node2
                node1 = node1.next
                node2 = node2.next  
            counter += 1
        return prehead.next
        
from ListNode import LinkedList
if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList([1, 2, 3, 4, 5])
    l2 = LinkedList([3760,2881,7595,3904,5069,4421,8560,8879,8488,5040,5792,56,1007,2270,3403,6062])
    head = s.reverseBetween(l2.head, 2, 7)
    head.printAsList()
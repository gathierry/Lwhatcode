'''
http://fisherlei.blogspot.com/2013/11/leetcode-linked-list-cycle-ii-solution.html

还是采用一个走一步，一个走两步的办法

1 -> 2 -> ... -> x-1 -> x -> x+1 -> ... -> x+k -> ... -> x+y -| 
                              ^                               |
                              |-------------------------------|
                              
假设在 x+k 相遇
t  = x + n*y + k
2t = x + m*y + k

2x + 2ny + 2k = x + my + k
x + k = (m - 2n) * y

等于说，两个指针相遇以后，再往下走 x 步就回到Cycle的起点了
'''

class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head is None:
            return None
        node1 = head
        node2 = head
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 is node2:
                break
        if node2.next is None or node2.next.next is None:
            return None
        # go x step
        node1 = head
        while node1 is not node2:
            node1 = node1.next
            node2 = node2.next
        return node1
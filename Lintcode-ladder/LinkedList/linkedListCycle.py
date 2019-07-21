'''
两个指针，一个前进1，一个前进2，如果追上了就说明有循环
'''

class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        node1 = head
        node2 = head
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next
            if node1 is node2:
                return True
        return False
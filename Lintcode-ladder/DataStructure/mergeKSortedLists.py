'''
解法一：
将 k 个链表分成两组 k/2 的进行排序。思路类似于归并排序
时间复杂度 T(k) = 2*T(k/2) + O(kn)
= (...((T(1) + O(2n)) + O(4n)) + ... ) + O(kn)
= O(n) + O(2n) + O(4n) + ... + O(kn)
= O(nk*logk)

解法二：
这种方法用到了堆的数据结构。
维护一个大小为k的堆，每次取堆顶的最小元素放到结果中，然后读取该元素的下一个元素放入堆中，重新维护好。
因为每个链表是有序的，每次又是去当前k个元素中最小的，所以当所有链表都读完时结束，这个时候所有元素按从小到大放在结果链表中。
这个算法每个元素要读取一次，即是k*n次，然后每次读取元素要把新元素插入堆中要logk的复杂度，所以总时间复杂度是O(nklogk)。空间复杂度是堆的大小，即为O(k)
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

def mergeTwoLists(l1, l2):
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


import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if len(lists) == 0:
            return None
        if len(lists) == 2:
            return mergeTwoLists(lists[0], lists[1])
        if len(lists) == 1:
            return lists[0]
        m = len(lists) // 2
        l1 = self.mergeKLists(lists[:m])
        l2 = self.mergeKLists(lists[m:])
        return mergeTwoLists(l1, l2)
        

    def mergeKLists2(self, lists):
        # write your code here
        heap = []
        for l in lists:
            if l:
                heap.append(l)
        heapq.heapify(heap)  # NEED TO ADD __lt__ FOR CLASS NODELIST
        virtual_head = ListNode(0)
        n = virtual_head
        while len(heap) > 0:
            node = heapq.heappop(heap)
            if node:
                n.next = node
                n = n.next
                if node.next:
                    heapq.heappush(heap, node.next)
        return virtual_head.next
        
    
        


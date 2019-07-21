'''
要求进行归并排序和快速排序，那就先来复习一下排序算法
归并排序：将数组不断二分，指导只剩一个或两个元素时排成有序数组，再按序合并。稳定，空间复杂度 O(n), 时间复杂度 O(nlogn)
快速排序：以最后一个元素为基准，小于它的往前放，大于它的往后放，形成 [<A, <A, <A, A,>A, >A, >A]，再对左右两个子序列进行同样的操作。不稳定，快排的空间复杂度是 O(logn)，因为快排的实现是递归调用的，时间复杂度平均 O(nlogn), 最坏 O(n^2)
'''

def _merge(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if i < len(a):
        c += a[i:]
    else:
        c += b[j:]
    return c

def mergeSort(A):
    l = len(A)
    if l == 1:
        return A
    if l == 2:
        return [min(A), max(A)]
    a = mergeSort(A[:l//2])
    b = mergeSort(A[l//2:])
    return _merge(a, b)
    
    
def partition(array, left, right):
    i = left-1
    for j in range(left, right):
        if array[j] <= array[right]:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[right] = array[right], array[i+1]
    return i+1

def quicksort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot-1)
        quicksort(array, pivot+1, right)
    return array
    
# =======================================================
    





from ListNode import ListNode

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    # merge sort
    def _mergeTwoLists(self, l1, l2):
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
        
    def sortList1(self, head):
        # write your code here
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            if head.val > head.next.val:
                newhead = head.next
                head.next.next = head
                head.next = None
                return newhead
            else:
                return head
        # get mid
        node1 = head
        node2 = head
        while node2.next and node2.next.next:
            node1 = node1.next
            node2 = node2.next.next
        mid = node1.next
        node1.next = None
        a = self.sortList(head)
        b = self.sortList(mid)
        return self._mergeTwoLists(a, b)
        
    # quick sort
    def _partition(self, head, x):
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
        node1.next = None
        return prehead.next, head
        
    def _uniqueValue(self, head):
        node = head
        while node:
            if node.val != head.val:
                return False
            node = node.next
            
        return True
    
    def sortList(self, head):
        # write your code here
        if head is None:
            return None
        if self._uniqueValue(head):
            return head
        x = head.val
        head, pivot = self._partition(head, x)
        
        h1 = self.sortList(head)
        h2 = self.sortList(pivot.next)
        newhead = h1
        if h1 is None:
            newhead = pivot
            if h2:
                pivot.next = h2
        else:
            while h1.next:
                h1 = h1.next
            h1.next = pivot
            if h2:
                pivot.next = h2
        return newhead
            
    
        
                
        
        
        


from ListNode import LinkedList
if __name__ == '__main__':
    A = [39, 27, 43, 3, 9, 82, 10]
    A = [1,2,3]*1000
    #print(mergeSort(A))
    #print(quicksort(A, 0, len(A)-1))
    s = Solution()
    l = LinkedList(A)
    head = s.sortList(l.head)
    head.printAsList()
    
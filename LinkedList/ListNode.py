
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def printAsList(self):
        A = []
        node = self
        while node is not None:
            A.append(node.val)
            node = node.next
        print(A)
        
class LinkedList:
    def __init__(self, A):
        next = None
        for i in range(len(A)-1, -1, -1):
            node = ListNode(A[i], next)
            next = node
        self.head = node
        
if __name__ == '__main__':
    llist = LinkedList([1,2,3,4,5])
    llist.head.printAsList()
    
        
        
        

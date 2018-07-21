
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    
    def printAsList(self):
        A = []
        B = []
        node = self
        while node is not None:
            A.append(node.label)
            B.append(node.random.label)
            node = node.next
        print(A)
        

    
        
        
        

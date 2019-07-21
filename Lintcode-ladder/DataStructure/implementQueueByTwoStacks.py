'''
stack 1: 底 12345 顶
stack 2: 
push: 加入 stack1
pop: 如果 stack2 不是空的，就从 stack2 里弹栈，否则将 stack1 倒入 stack2 再弹
'''


class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    def transfer(self):
        if len(self.stack2) == 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.transfer()
        return self.stack2.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self.transfer()
        return self.stack2[-1]
        

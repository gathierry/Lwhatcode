'''
A -> B -> C -> D
先复制每一个元素插入到原来的后边
A -> a -> B -> b -> C -> c -> D -> d
之后复制 random
最后断开连接
'''


from RandomListNode import RandomListNode

class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        node = head
        while node:
            node2 = RandomListNode(node.label)
            node2.next = node.next
            node.next = node2
            node = node2.next
        node = head
        node2 = head.next
        while node:
            random = node.random
            if random:
                node2.random = random.next  
            node = node.next.next
            if node:
                node2 = node2.next.next
        node2 = head.next
        while node2.next:
            tmp = node2.next.next
            node2.next = tmp
            node2 = tmp
        newhead = head.next
        return newhead
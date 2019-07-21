'''
因为没有要求顺序保持不变
可以每当遇到 elem 时，就将 elem 与队尾的数交换，同时数组长度 -1
'''

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        k = 0
        while k < len(A):
            if A[k] == elem:
                A[k], A[-1] = A[-1], A[k]
                A = A[:-1]
            else:
                k += 1
        print(A)
        return k
            
if __name__ == '__main__':
    solution = Solution()
    A = [0,4,4,0,4,4,4,0,2]
    elem = 4
    print(solution.removeElement(A, elem))
    print(A)
'''
从后往前扫描
'''

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                print(i, j)
                A[k] = B[j]
                j -= 1
            k -= 1
        if j < 0:
            return
        else:
            A[:k+1] = B[:j+1]
        print(A)
    
    
if __name__ == '__main__':
    solution = Solution()
    A = [3,4,6,None,None,None]
    m = 3
    B = [1,2,5]
    n = 3
    solution.mergeSortedArray(A, m, B, n)
        

'''
通过在数组内交换元素，将 i+1 放在 A[i] 的位置，最后遍历数组找到第一个不符合条件的 index
因为如果存在大于数组长度的数，那么中间一定有空隙
'''



class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        i = 0
        while i < len(A):
            if A[i] > 0 and A[i] <= len(A) and A[i] != i+1 and A[A[i] - 1] != A[i]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            else:
                i += 1
        for i, a in enumerate(A):
            if a != i+1:
                return i+1
        return len(A) + 1
        
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.firstMissingPositive([1,1]))
    #print(solution.firstMissingPositive([1,2,0]))
    #print(solution.firstMissingPositive([3,4,-1,1]))
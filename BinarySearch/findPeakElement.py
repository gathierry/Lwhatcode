class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        lb = 0
        ub = len(A) - 1
        while lb < ub:
            m = (lb + ub) // 2
            if A[m] > A[m-1] and A[m] > A[m+1]:
                return m
            elif A[m] > A[m-1] and A[m] < A[m+1]:
                lb = m
            elif A[m] < A[m-1] and A[m] > A[m+1]:
                ub = m
            else:
                lb = m
            print(lb, ub)
        
if __name__ == '__main__':
    solution = Solution()
    #print(solution.findPeak([1, 2, 1, 3, 4, 5, 7, 6]))
    print(solution.findPeak([1, 10, 9, 8, 7, 6, 5, 4]))
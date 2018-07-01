'''
用二分法时，分两种情况考虑，即 max 在 mid 左边和 max 在 mid 右边
'''


class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        lb = 0
        ub = len(A) - 1
        while lb <= ub:
            m = (lb + ub) // 2
            if A[m] < A[ub]:
                if A[m] > target:
                    ub = m - 1
                elif A[m] < target:
                    if A[ub] > target:
                        lb = m + 1
                    elif A[ub] < target:
                        ub = m - 1
                    else:
                        return ub
                else:
                    return m
            elif A[m] > A[ub]:
                if A[m] < target:
                    lb = m + 1
                elif A[m] > target:
                    if A[lb] < target:
                        ub = m - 1
                    elif A[lb] > target:
                        lb = m + 1
                    else:
                        return lb
                else:
                    return m
            else:
                if A[m] == target:
                    return m
                else:
                    break
        return -1
                
if __name__ == '__main__':
    solution = Solution()
    print(solution.search([4, 5, 1, 2, 3], 4))
    print(solution.search([4, 5, 1, 2, 3], 0))
    print(solution.search([5], 5))
    print(solution.search([3,4,5,6,7,8], 7))
    print(solution.search([0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1], -9))
                
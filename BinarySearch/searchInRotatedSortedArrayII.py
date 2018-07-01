'''
同样的，这次引入了 duplicate
应对方法也相同，左右相等无法判断时将右边界 -1
'''

class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return False
        lb = 0
        ub = len(A) - 1
        while lb <= ub:
            if A[lb] == A[ub]:
                ub -= 1
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
                        return True
                else:
                    return True
            elif A[m] > A[ub]:
                if A[m] < target:
                    lb = m + 1
                elif A[m] > target:
                    if A[lb] < target:
                        ub = m - 1
                    elif A[lb] > target:
                        lb = m + 1
                    else:
                        return True
                else:
                    return True
            else:
                if A[m] == target:
                    return True
                else:
                    break
        return A[lb] == target


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([1, 1, 0, 1, 1, 1], 0))
    print(solution.search([1, 1, 1, 1, 1, 1], 0))
    print(solution.search([2,2,2,3,1], 1))
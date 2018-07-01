'''
在 0 ~ l-1 之间二分搜索
'''


class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0 or target < A[0]:
            return 0
        if target > A[-1]:
            return len(A)
        lb = 0
        ub = len(A) - 1
        while lb < ub:
            mid = (lb + ub) // 2
            if A[mid] < target:
                lb = mid + 1
            elif A[mid] > target:
                ub = mid
            else:
                return mid
        return lb
        


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1], 0))
    print(solution.searchInsert([1,3,5,6], 5))  #2
    print(solution.searchInsert([1,3,5,6], 2))  #1
    print(solution.searchInsert([1,3,5,6], 7))  #4
    print(solution.searchInsert([1,3,5,6], 0))  #0
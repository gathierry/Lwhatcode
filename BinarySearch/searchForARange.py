class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        # left
        lb = 0
        rb = len(A) - 1
        while lb < rb:
            m = (lb + rb) // 2
            if target < A[m]:
                rb = m - 1
            elif target > A[m]:
                lb = m + 1
            else:
                rb = m
        idx1 = rb
        # right
        lb = 0
        rb = len(A) - 1
        while lb < rb:
            m = (lb + rb) // 2 + 1  # 因为平均值可能落到lb上却不能rb上， 为了避免无限循环，这里+1
            if target < A[m]:
                rb = m - 1
            elif target > A[m]:
                lb = m + 1
            else:
                lb = m
        idx2 = lb

        if A[idx1] != target:
            return [-1, -1]
        return [idx1, idx2]

                
if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 7,8, 8, 10], 9))
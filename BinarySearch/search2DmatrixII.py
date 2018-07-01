'''
The challenge is O(m+n) time and O(1) extra space
这道题的约束更少，只说同一行左到右递增，同一列上到下递增
从右上角开始，如果大于 target，则这一列可排除；如果小于target，则这一行可排除
因为同一行或同一列没有duplicate，所以如果等于，计数器 +1，右上角向左下各移一步
'''


class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        n = len(matrix)  # row
        if n == 0:
            return 0
        m = len(matrix[0])  # column
        i = 0
        j = m - 1
        counter = 0
        while i < n and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                counter += 1
                j -= 1
                i += 1
        return counter
        
if __name__ == '__main__':
    solution = Solution()
    m = [[1, 3, 5, 7], [2, 4, 7, 8], [3, 5, 9, 10]]
    print(solution.searchMatrix(m, 3))

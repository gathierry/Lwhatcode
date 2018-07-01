'''
先确定在哪一行，之后在行内寻找，都用二分查找，复杂度 O(log(n) + log(m))
'''

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        lr = 0
        ur = m - 1
        # determine the row
        while lr < ur:
            mr = (lr + ur) // 2
            if target < matrix[mr][0]:
                ur = mr - 1
            elif target > matrix[mr][n - 1]:
                lr = mr + 1
            else:
                lr = mr
                break
        # determine the column
        lc = 0
        uc = n - 1
        while lc < uc:
            mc = (lc + uc) // 2
            if target < matrix[lr][mc]:
                uc = mc - 1
            elif target > matrix[lr][mc]:
                lc = mc + 1
            else:
                return True
        return target == matrix[lr][lc]
        
if __name__ == '__main__':
    solution = Solution()
    #m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    #print(solution.searchMatrix(m, 4))
    m2 = [[1,8,11,15,18,19,24,31,36,40,42,47,51,52,57,58,61,65,67],\
          [84,108,130,145,166,177,202,217,233,253,265,284,300,313,324,348,367,391,401],\
          [422,442,453,476,496,516,532,544,567,588,611,625,641,653,673,695,705,727,748],\
          [764,778,795,805,823,841,857,876,890,907,932,954,974,992,1005,1019,1034,1053,1078],\
          [1100,1117,1129,1144,1160,1178,1203,1220,1233,1244,1256,1268,1290,1310,1322,1339,1351,1367,1391],\
          [1413,1429,1444,1456,1467,1484,1509,1521,1539,1549,1561,1586,1602,1621,1639,1664,1681,1706,1722]]
    print(solution.searchMatrix(m2, 1224))










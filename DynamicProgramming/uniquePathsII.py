'''
递归，第一次向右 + 第一次向下 会超时
另一种做法，s[i][j] = s[i-1][j] + s[i][j-1], 依次计算布满地图即可；第一行和第一列，一旦遇到 obstacle，后面都是 0
'''

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                res[i][0] == 0
                break
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                res[0][i] = 1
            else:
                res[0][i] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: res[i][j] = 0
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]

class Solution1:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        return self.go(obstacleGrid, 0, 0)
            
            
    def go(self, obstacleGrid, row, col):
        if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
            return 1
        if obstacleGrid[row][col] == 1:
            return 0
        right = 0
        down = 0
        if col < len(obstacleGrid[0]) - 1:
            right = self.go(obstacleGrid, row, col+1)
        if row < len(obstacleGrid) - 1:
            down = self.go(obstacleGrid, row+1, col)
        return right + down
        
if __name__ == '__main__':
    s = Solution()
    og = [[0,0,0],[0,1,0],[0,0,0]]
    og = [
        [0,0,0,0,0,0,0,0,1,0,0,0],         
        [0,0,0,1,0,1,0,0,0,0,0,1],
        [0,0,0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0]]
    print(s.uniquePathsWithObstacles(og))
    
        

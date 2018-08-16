'''
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


     [a],
    [b,c],
   [d,e,f],
  [g,h,i,j]

s[r][0] = s[r-1][0] + x
s[r][c] = min(s[r-1][c-1], s[r-1][c]) + x
s[r][-1] = s[r-1][-1] + x



'''

class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        res = [0 for k in range(n)]
        res[0] = triangle[0][0]
        for r in range(1, n):
             # no need to use tmp if do this in reversed order
            res[r] = res[r-1] + triangle[r][r]
            for c in range(r-1, 0, -1):
                res[c] = min(res[c-1], res[c]) + triangle[r][c]
            res[0] = res[0] + triangle[r][0]
        return min(res)
        
if __name__ == "__main__":
    s = Solution()
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(s.minimumTotal(triangle))
        

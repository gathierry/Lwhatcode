'''
假设字符串 a, 共 m 位，从 a[1] 到 a[m]
字符串 b, 共 n 位，从 b[1] 到 b[n]
d[i][j] 表示字符串 a[1]-a[i] 转换为 b[1]-b[j] 的编辑距离

- 当 a[i] 等于 b[j] 时，d[i][j] = d[i-1][j-1]
- 当 a[i] 不等于 b[j] 时，d[i][j] 等于如下 3 项的最小值
    - d[i-1][j] + 1（删除 a[i]）
    - d[i][j-1] + 1（插入 b[j])
    - d[i-1][j-1] + 1（将 a[i] 替换为 b[j]）

d[i][0] = i，此时 b 为空，需要删除 a[1]-a[i]
d[0][j] = j 同理

   j  0  1  2  3  ... m
i
0     0  1  2  3      m
1     1
2     2
3     3
...
n     n
'''


class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        m = len(word1)
        n = len(word2)
        d = [k for k in range(m+1)]
        for i in range(1, n+1):
            dd = [i for k in range(m+1)]
            for j in range(1, m+1):
                if word2[i-1] == word1[j-1]:
                    dd[j] = d[j-1]
                else:
                    dd[j] = min(d[j]+1, dd[j-1]+1, d[j-1]+1)
            d = dd.copy()
        return d[m]
        
if __name__ == '__main__':
    s = Solution()
    w1 = 'mart'
    w2 = 'karma'
    print(s.minDistance(w1, w2))
            

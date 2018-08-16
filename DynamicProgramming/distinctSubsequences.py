'''
假设字符串 S, 共 m 位，从 s[1] 到 s[m]
字符串 T, 共 n 位，从 T[1] 到 T[n]
d[i][j] 表示 T[1]-T[j] 中 S[1]-S[i] 这个子字符串的个数

e.g.
  S Ø r a b b b i t
T
Ø   1 1 1 1 1 1 1 1
r   0 1 1 1 1 1 1 1
a   0 0 1 1 1 1 1 1
b   0 0 0 1 2 3 3 3
b   0 0 0 0 1 3 3 3
i   0 0 0 0 0 0 3 3
t   0 0 0 0 0 0 0 3

rabbbit 中就有三个 rabbit 的子串 (rab1b2it, rab2b3it, rab1b3it)

- 当 S[i] 等于 T[j] 时，d[i][j] = d[i][j-1] + d[i-1][j-1]
- 当 S[i] 不等于 T[j] 时，d[i][j] = d[i][j-1]
'''

class Solution:
    """
    @param: : A string
    @param: : A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        # write your code here
        m = len(S)
        n = len(T)
        d = [1 for k in range(m+1)]
        for i in range(1, n+1):
            dd = [0 for k in range(m+1)]
            for j in range(1, m+1):
                if T[i-1] == S[j-1]:
                    dd[j] = dd[j-1] + d[j-1]
                else:
                    dd[j] = dd[j-1]
            d = dd.copy()
        return d[m]
        
if __name__ == '__main__':
    s = Solution()
    S = 'rabbbit'
    T = 'rabbit'
    print(s.numDistinct(S, T))
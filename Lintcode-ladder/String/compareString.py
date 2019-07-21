"""
Description
Compare two strings A and B, determine whether A contains all of the characters in B.
The characters in string A and B are all Upper Case letters.
The characters of B in A are not necessary continuous or ordered.

Example
For A = "ABCD", B = "ACD", return true.
For A = "ABCD", B = "AABC", return false.
"""

'''
这道题可以用与 valid anagram 相同的算法来解
建立哈希表，因为字符种类有限，所以空间复杂度是 O(1)
输入的s, t都只遍历一遍，时间复杂度是 O(n)

解法二：
将A变成set
遍历B，在A中找是否存在
但是这种解法无法处理相同字母多次出现的情况
如
A="ABCDEFG"
B="ACC"
'''

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        # write your code here
        if len(A) < len(B):
            return False
        d = {}
        for a in A:
            if a not in d:
                d[a] = 0
            d[a] += 1
        for b in B:
            if b not in d:
                return False
            d[b] -= 1
            if d[b] < 0:
                return False
        return True
        
    def compareStrings2(self, A, B):
        # write your code here
        if len(A) < len(B):
            return False
        sa = set(A)
        for b in B:
            if b not in sa:
                return False
        return True
        
if __name__ == '__main__':
    solution = Solution()
    
    A = "ABCD"
    B = "ACD"
    print(solution.compareStrings2(A, B))
    
    A = "ABCD"
    B = "AABC"
    print(solution.compareStrings(A, B))
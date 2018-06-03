'''
这道题可以用与 valid anagram 相同的算法来解
建立哈希表，因为字符种类有限，所以空间复杂度是 O(1)
输入的s, t都只遍历一遍，时间复杂度是 O(n)
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
        
        
if __name__ == '__main__':
    solution = Solution()
    
    A = "ABCD"
    B = "ACD"
    print(solution.compareStrings(A, B))
    
    A = "ABCD"
    B = "AABC"
    print(solution.compareStrings(A, B))
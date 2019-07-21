"""
Description
Given k strings, find the longest common prefix (LCP).

Example
For strings "ABCD", "ABEF" and "ACEF", the LCP is "A"
For strings "ABCDEFG", "ABCEFG" and "ABCEFA", the LCP is "ABC"
"""

'''
暴力算法即可，注意最长前缀长度不可能大于最短字符串
'''

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) == 0:
            return ''
        i = 0
        prefix = ''
        while True:
            for k, s in enumerate(strs):
                if len(s) == 0:
                    return ''
                if len(s) == i:
                    return prefix
                if k == 0:
                    prefix += s[i]
                if s[i] != prefix[-1]:
                     return prefix[:-1]
            i += 1
            
if __name__ == '__main__':
    solution = Solution()
    
    s = ["ABCD", "ABEF", "ACEF"]
    print(solution.longestCommonPrefix(s))
    
    s = ["ABCDEFG", "ABCEFG", "ABCEFA"]
    print(solution.longestCommonPrefix(s))
    
    s = ["ABC"]
    print(solution.longestCommonPrefix(s))
    
    s = ["abc", "abcd", "", "ab", "ac"]
    print(solution.longestCommonPrefix(s))
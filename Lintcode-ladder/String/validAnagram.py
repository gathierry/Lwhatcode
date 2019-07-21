"""
Description
Write a method anagram(s,t) to decide if two strings are anagrams or not.

Clarification
What is Anagram?
Two strings are anagram if they can be the same after change the order of characters.
Example
Given s = "abcd", t = "dcab", return true.
Given s = "ab", t = "ab", return true.
Given s = "ab", t = "ac", return false.

Challenge
O(n) time, O(1) extra space
"""

'''
方法一：
建立哈希表，因为字符种类有限，所以空间复杂度是 O(1)
输入的s, t都只遍历一遍，时间复杂度是 O(n)
方法二：
对两个字符串分别排序，然后对比，时间复杂度 O(nlogn)，空间复杂度 O(logn)
'''

class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        if len(s) != len(t):
            return False
        d = {}
        for sc in s:
            if sc not in d:
                d[sc] = 0
            d[sc] += 1
        for tc in t:
            if tc not in d:
                return False
            d[tc] -= 1
            if d[tc] < 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    
    s = "abcd"
    t = "dcab"
    print(solution.anagram(s, t))
    
    s = "ab"
    t = "ab"
    print(solution.anagram(s, t))
    
    s = "ab"
    t = "ac"
    print(solution.anagram(s, t))
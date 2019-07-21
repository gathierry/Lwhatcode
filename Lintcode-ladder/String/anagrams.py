"""
Description
Given an array of strings, return all groups of strings that are anagrams.
All inputs will be in lower-case

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].
Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Challenge
What is Anagram?
Two strings are anagram if they can be the same after change the order of characters.
"""

'''
因为要将 anagram 选取出来，必然需要相互比较。
在 valid anagram 中提到了两个方法，这里用第二种，排序的方法较为简便。
先对所有字符串进行排序
以排序后的字符串 so 作为 key, 排序前的字符串 [s1, s2] 作为 value 构建 dict
时间复杂度 O(knlogn) 空间复杂度 O(kn) -- k 为字符串个数，n 为单个字符串长度
'''

class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        d = {}
        for st in strs:
            so = ''.join(sorted(st))
            if so not in d:
                d[so] = []
            d[so].append(st)
        result = []
        for k, v in d.items():
            if len(v) > 1:
                result += v
        return result
        
if __name__ == '__main__':
    solution = Solution()
    
    s = ["lint", "intl", "inlt", "code"]
    print(solution.anagrams(s))

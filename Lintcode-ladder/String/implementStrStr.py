"""
Description
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Clarification
Do I need to implement KMP Algorithm in a real interview?
Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. 
But make sure you confirm with the interviewer first.

Example
If source = "source" and target = "target", return -1.
If source = "abcdabcdefg" and target = "bcd", return 1.

Challenge
O(n^2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
"""

'''
最直观的方法是复杂度为 O(n^2) 的方法，对于 source 每一位都向后匹配，直到匹配成功
'''


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        if len(target) == 0:
            return 0
        si = 0
        ti = 0
        for si in range(len(source) - len(target) + 1):
            for ti in range(len(target)):
                if target[ti] == source[si + ti]:
                    if ti == len(target) - 1:
                        return si
                else:
                    break
        return -1
        
'''
KMP 算法的时间复杂度为 O(m+n)。它首先将问题的中心转移为，寻找 target 每个从头开始的子串上，最长的前缀和后缀的匹配
这里可以参见知乎的解释 https://www.zhihu.com/question/21923021

所以，令主字符串为 t，匹配字符串为 p
问题变成，已知 p[j] != t[i], p[0:j] == t[i-j:i], 求映射 Next(j)
假设已知 Next(j-1) = k1, 即 p[0:k1] = p[j-1-k1:j-1]
        若 p[j-1] = p[k1]，则 Next(j) = k1+1
        若 p[j-1] != p[k1]，则只能从 p[0:k1] 这个区间找 Next(j) 的值
            那么尝试 Next(k1) = k2
            若 k2==0，递归结束
            若 k2!=0，k2 前面一小段与 j-1 前面一小段相同，即 p[0:k2]=p[k1-k2:k1]=p[j-1-k2:j-1]，递归到上一层判断
'''

class KMP_Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
        if target == '':
            return 0
        if source == '':
            return -1
        i = 0
        j = 0
        next_list = self.getNext(target)
        while i < len(source) and j < len(target):
            if source[i] == target[j] or j == -1:
                i += 1
                j += 1
            else:
                j = next_list[j]
        if j == len(target):
            return i-j
        return -1
        
        
    def getNext(self, pattern):
        next_list = [0 for _ in range(len(pattern))]
        j = 0
        k = -1
        next_list[j] = k
        while j < len(pattern) - 1:
            if pattern[j] == pattern[k] or k == -1:
                j += 1
                next_list[j] = k + 1
                k = next_list[j]
            else:
                k = next_list[k]
        return next_list
        
        
        
if __name__ == '__main__':
    solution = Solution()
    
    source = "source"
    target = "target"
    print(solution.strStr(source, target))
    
    source = "abcdabcdefg"
    target = "bcd"
    print(solution.strStr(source, target))
    
    source = "tartarget"
    target = "target"
    print(solution.strStr(source, target))
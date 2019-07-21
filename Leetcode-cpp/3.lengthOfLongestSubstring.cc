/**
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
*/

/**
给定字符串 S = s0 s1 s2 ... sn
我们希望有一个哈希表 d = {s_i: i, ..., s_j-1: j-1} 表示当前探索子字符串 i 到 j
一个整数 l 记录最长距离
如果 s_j 与 当前探索的子字符串中有重复，即：s_j 与 d 中的 s_k 相同且 k > i
则 记录 l，并且从 k 的下一位开始重新探索 i->k+1
当 j 到达末尾时，最长的 j-i+1 即为结果
*/

#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
		if (s.size() == 0) {
			return 0;
		}
        unordered_map<char, size_t> d;
		size_t l = 1;
		d[s[0]] = 0;
		for(size_t i = 0, j = 1; j < s.size(); ++j) {
			char c = s[j];
		    if (d.find(c) != d.end()) {
				size_t k = d[c];
				i = max(k+1, i);
		    }
			d[c] = j;
			l = max(l, j - i + 1);
		}
		return l;
    }
};

int main() {
	string s = "pwwkew";
	Solution solution;
	int l = solution.lengthOfLongestSubstring(s);
	cout << l << endl;
	return 0;
}
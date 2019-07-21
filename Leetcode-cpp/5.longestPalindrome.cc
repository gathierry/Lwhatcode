/**
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
*/

/**
遍历所有情况，对与每一个中心点，分别向左右各自外扩，每一步都可以判断是否是回文串
对于字符串
s0 s1 s2 ... s_n
来说，中心点有
s0, s0.5, s1, s1.5, ... s_n-0.5, s_n
共 n+(n-1)=2n-1 个

对每个中心点，计算最长回文串长度，如
s_i 长度 l
若 l 为奇数，应取子字符串 s_i-l/2, ... s_i, ... s_i+l/2
若 l 为偶数，应取子字符串 s_(i-0.5)-(l/2-1), ..., s_(i-0.5), s(i+0.5), ..., s(i-0.5)+(l/2)

时间复杂度 O(n2)
*/


#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
	int lenPalindrome(string s, int lcenter, int rcenter) {
		if (lcenter != rcenter && s[lcenter] != s[rcenter]) {
			return 1;
		}
		while (lcenter >= 0 && rcenter < s.size()) {
			if (s[lcenter] == s[rcenter]) {
				lcenter --;
				rcenter ++;
			} else {
				break;
			}
		}
		return (rcenter - 1) - (lcenter + 1) + 1;
		
	}
	
    string longestPalindrome(string s) {
		if (s.size()==0) {
			return "";
		}
		string res = s.substr(0, 1);
		for (size_t i = 0; i < s.size()-1; ++i) {
			int l1 = lenPalindrome(s, i, i);
			int l2 = lenPalindrome(s, i, i + 1);
			if (l1 > l2 && l1 > res.size()) {
				res = s.substr(i-l1/2, l1);
			}
			if (l2 > l1 && l2 > res.size()) {
				res = s.substr(i-l2/2+1, l2);
			}
		}
		return res;
    }
};


int main() {
	//string s = "babad";
	//string s = "cbbd";
	string s = "";
	Solution solution;
	string l = solution.longestPalindrome(s);
	cout << l << endl;
	return 0;
}
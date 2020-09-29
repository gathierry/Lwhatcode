/**
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例1:
输入: ["flower","flow","flight"]
输出: "fl"

示例2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
*/
/**

*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0) {
			return "";
		}
		string ref_str = strs[0];
		string common_prefix = "";
		for (size_t j = 0; j < ref_str.size(); ++j) {
			bool c = true;
	        for (size_t i = 1; i < strs.size(); ++i) {
				if (strs[i].size() <= j) {
					c = false;
					break;
				} else {
					if (strs[i][j] != ref_str[j]) {
						c = false;
						break;
					}
				}
	        }
			if (c) {
				common_prefix += ref_str[j];
			} else {
				break;
			}
		}
		return common_prefix;
    }
};

int main() {
	vector<string> strs{"flower", "flow", "flight"};
	Solution solution;
	string res = solution.longestCommonPrefix(strs);
	cout << res << endl;
	return 0;
}
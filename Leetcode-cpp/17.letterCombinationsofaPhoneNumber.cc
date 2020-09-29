/**
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
*/
/**
因为要枚举所有情况
假设输入是 a1 a2 ... an
那么就是 n 重循环，然而 n 是可变的
尝试用递归解决，时间复杂度 O(3^n)
使用回溯，`backtrack(combination, next_digits)` 将目前已经产生的组合与下一个数字作为参数
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
	void backtrack(unordered_map<char, string> &phone, string combined, string digits, int cur, vector<string> &ret) {
		if (cur < digits.size()) {
			string cs = phone.find(digits[cur])->second;
			for (size_t j = 0; j < cs.size(); ++j) {
				backtrack(phone, combined+cs.substr(j, 1), digits, cur+1, ret);
			}
		}
		else {
			ret.push_back(combined);
		}
	}

    vector<string> letterCombinations(string digits) {
		unordered_map<char, string> phone;
		phone['2'] = "abc";
		phone['3'] = "def";
		phone['4'] = "ghi";
		phone['5'] = "jkl";
		phone['6'] = "mno";
		phone['7'] = "pqrs";
		phone['8'] = "tuv";
		phone['9'] = "wxyz";

        vector<string> ret{};
		if (digits.size() == 0) {
			return ret;
		}
		backtrack(phone, "", digits, 0, ret);
		return ret;
    }
};

int main() {
	string digits = "23";
	Solution solution;
	vector<string> res = solution.letterCombinations(digits);
	for (size_t i = 0; i < res.size(); ++i) {
		cout << res[i] << ", ";
	}
	return 0;
}
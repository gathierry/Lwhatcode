/**
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

*/
/**
令字符串 s0, ... sn
行数 N
输出(Z中间的空格已被忽略掉)

s0                  s_2N-2
s1     s_N+(N-2-1)  s_2N-1
s2     s_N+(N-2-2)  s_2N
.      .            .
s_k    s_N+(N-2-k)  s_2N+(k-2)
.      .            .
s_N-2  s_N          s_2N+(k-2)+(N-2-k)
s_N-1               s_2N+(k-2)+(N-1-k)
化简
s0               s_2N-2              s_4N-4
s1     s_2N-3    s_2N-1    s_4N-5    .
s2     s_2N-4    s_2N      s_4N-6    .
.      .         .         .         .
s_k    s_2N-2-k  s_2N-2+k  s_4N-4-k  s_4N-4+k
.      .         .         .         .
s_N-2  s_N       s_3N-4    s_3N-2    .
s_N-1            s_3N-3              s_5N-5

Corner case: N=1 时，直接返回原始输入

*/


#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
		if (numRows == 1) {
			return s;
		}
        string res = "";
		for (int i = 0; i < s.size(); i += 2 * numRows - 2) {
			res += s.substr(i, 1);
		}
		for (int k = 1; k < numRows - 1; ++k) {
			int j = k;
			while (j < s.size()) {
				res += s.substr(j, 1);
				j += 2 * (numRows - 1 - k);
				if (j >= s.size()) {
					break;
				}
				res += s.substr(j, 1);
				j += 2 * k;
			}
		}
		for (int i = numRows - 1; i < s.size(); i += 2 * numRows - 2) {
			res += s.substr(i, 1);
		}
		return res;
    }
};

int main() {
	//string s = "LEETCODEISHIRING";
	string s = "A";
	Solution solution;
	string s2 = solution.convert(s, 1);
	cout << s2 << endl;
	return 0;
}
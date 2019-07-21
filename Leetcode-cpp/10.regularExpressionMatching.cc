/**
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
*/
/**

      p[:0]  p[:1] ... p[:n]

s[:0]  1
s[:1]  0
s[:2]  0
...
s[:m]  0

if s[i] = p[j]: dp[i][j] = dp[i-1][j-1]
if p[j] = '.': dp[i][j] = dp[i-1][j-1]
if p[j] = '*':
    if p[j-1] != s[i] (*只能代表上一字母出现0次): dp[i][j] = dp[i][j-2]
    if p[j-1] = s[i]
        *代表上一字母出现0次 dp[i][j] = dp[i][j-2] 或
        *代表上一字母出现1次 dp[i][j] = dp[i][j-1] 或
        *代表上一字母出现>1次，dp[i][j] = dp[i-1][j]

*/

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        size_t m = s.size();
		size_t n = p.size();
		if (n == 0) {
			return m == 0;
		}
		if (m == 0) {
			if (n == 0) {
				return true;
			}
			if (n % 2 == 1) {
				return false;
			}
			for (size_t i = 1; i < n; i+=2) {
				if (p[i] != '*') {
					return false;
				}
			}
			return true;
		}
		bool dp[m+1][n+1];
		for (size_t i = 0; i <= m; ++i) {
			for (size_t j = 0; j <= n; ++j) {
				// first column
				if (j == 0) {
					dp[i][j] = (i == 0);
					continue;
				}
				// first row
				if (i == 0) {
					if (j == 1) {
						if (n > 1) {
							dp[i][j] = (p[j] == '*');
						} else {
							dp[i][j] = false;
						}
						
					}
					else {
						dp[i][j] = dp[i][j-1] && (p[j-1] == '*' || ((n > j + 1) && p[j] == '*'));
					}
					continue;
				}
				if (s[i-1] == p[j-1] || p[j-1] == '.') {
					dp[i][j] = dp[i-1][j-1];
				} else if (p[j-1] == '*') {
					if (p[j-2] != '.' && p[j-2] != s[i-1]) {
						dp[i][j] = dp[i][j-2];
					} else {
						dp[i][j] = dp[i][j-1] || dp[i-1][j];
						if (j > 1) {
							dp[i][j] = dp[i][j] || dp[i][j-2];
						}
					}
				} else {
					dp[i][j] = false;
				}
				
			}
		}
	
		// ====== DEBUG ======
		for (size_t i = 0; i <= m; ++i) {
			for (size_t j = 0; j <= n; ++j) {
				cout << dp[i][j] << " ";
			}
			cout << endl;
		}
		// ====== DEBUG END ======
		
		return dp[m][n];
    }
};

int main() {
	string s0 = "mississippi";
	string p0 = "mis*is*p*.";
	string s1 = "aab";
	string p1 = "c*a*b";
	string s2 = "ab";
	string p2 = ".*c";
	bool res;
	Solution solution;
	// res = solution.isMatch(s0, p0);
	// cout << res << endl;
	// res = solution.isMatch(s1, p1);
	// cout << res << endl;
	res = solution.isMatch(s2, p2);
	cout << res << endl;
	return 0;
}
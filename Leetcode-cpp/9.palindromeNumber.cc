/**
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
*/
/**
直观的思路是用第7题的办法，将整数翻转，与原来的数做对比。
但事实上，可以只反转一半的位数。这样也可以避免溢出的问题。
令 x 为原数字，y 为翻转的数字
当 x 和 y 只差 1 位时比较它们
若差 1 位且 x / 10 == y，则是
若差 0 位且 x == y，则是

简化成 x <= y 时，
x == y || x == y / 10

Corner case 除 0 以外 10 的 倍数
因为 k0000 翻转到最后会成为 x=0, y=k,也符合上述条件，但显然不是回文

*/

#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
		if (x < 0 || (x % 10 == 0 && x != 0)) {
			return false;
		}
		int y = 0;
		while (x > y) {
			int z = x % 10;
			x = x / 10;
			y = y * 10 + z;
		}
        return (x == y || x == y / 10);
    }
};

int main() {
	// int x = 121;
	int x = 20;
	// int x = -123;
	Solution solution;
	int res = solution.isPalindrome(x);
	cout << res << endl;
	return 0;
}
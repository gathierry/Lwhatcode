/**
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
*/
/**
对于一个 N 位整数 x = x0 x1 x2 ... xn，
可以看作一个 栈，个位是栈首
弹栈操作：x % 10 得到栈首数字 z, x / 10 得到弹栈后的内容。 负数取余得负数
进栈操作：y * 10 + z。y 表示栈内当前数字，z 表示要进栈的数字。
构造两个栈，可以将数字翻转。记得保留符号。

如果超出数值范围，返回 0. [-2147483648, 2147483647]
     y * 10 + z >= INT_MAX
<=>  y >= (INT_MAX - z) / 10
<=>  y > INT_MAX / 10 or (y = INT_MAX / 10 and z > 7)
同理，对于负数
     y * 10 + z <= INT_MIN
<=>  y <= (INT_MIN - z) / 10
<=>  y < INT_MIN / 10 or (y = INT_MIN / 10 and z < -8)


Corner case
若输入为 0， 则输出还是 0.
*/

#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
		int y = 0;
		while (x != 0) {
			int z = x % 10;
			x = x / 10;
			if (y > INT_MAX / 10 || (y == INT_MAX / 10 && z > 7)) {
				return 0;
			}
			if (y < INT_MIN / 10 || (y == INT_MIN / 10 && z < -8)) {
				return 0;
			}
			y = y * 10 + z;
		}
		return y;
    }
};

int main() {
	// int x = 123;
	// int x = 0;
	// int x = -123;
	// int x = 120;
	int x = -2147483648;
	Solution solution;
	int res = solution.reverse(x);
	cout << res << endl;
	return 0;
}
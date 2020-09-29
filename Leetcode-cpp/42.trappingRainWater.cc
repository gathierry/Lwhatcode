/**
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
*/
/**
方法一：
对于 1 到 n-1 的每个位置，都可以计算向左的最大值和向右的最大值
s_i = min(max_0^(i-1), max_(i+1)^n)
时间复杂度 O(n) 需遍历两遍
空间复杂度 O(n)

*/


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
		if (height.size() < 3) {
			return 0;
		}
        int lb[height.size()];
		int rb[height.size()];
		int lb_max = -1;
		int rb_max = -1;
		for (size_t i = 0; i < height.size(); ++i) {
			lb_max = max(lb_max, height[i]);
			lb[i] = lb_max;
			rb_max = max(rb_max, height[height.size() - 1 - i]);
			rb[height.size() - 1 - i] = rb_max;
		}
		int s = 0;
		for (size_t i = 1; i < height.size() - 1; ++i) {
			int c = min(lb[i-1], rb[i+1]) - height[i];
			c = max(0, c);
			s += c;
		}
		return s;
    }
};

int main() {
	vector<int> nums{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
	Solution solution;
	int res = solution.trap(nums);
	cout << res << endl;
	return 0;
}
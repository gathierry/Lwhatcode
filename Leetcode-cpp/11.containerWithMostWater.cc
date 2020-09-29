/**
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai)。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
*/
/**
最直接的暴力法要 O(n^2)
更简便的方法
可以维护两个指针，i, j, i=0, j=n-1
area_{i,j} = (j - i) * min(a[i], a[j])

将指向较短线段的指针向较长线段那端移动一步。
若 a[i] < a[j] 则 area[i, j-1] 一定小于 area[i, j]

记录整个过程中的最大值
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        size_t i = 0;
		size_t j = height.size() - 1;
		size_t max_area = 0;
		while (i < j) {
			max_area = max((j - i) * min(height[i], height[j]), max_area);
			if (height[i] < height[j]) {
				i ++;
			} else {
				j --;
			}
		}
		return max_area;
    }
};

int main() {
	vector<int> height{ 1, 8, 6, 2, 5, 4, 8, 3, 7};
	Solution solution;
	int res = solution.maxArea(height);
	cout << res << endl;
	return 0;
}
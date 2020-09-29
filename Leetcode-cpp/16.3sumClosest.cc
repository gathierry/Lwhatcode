/**
给定一个包括 n 个整数的数组 nums 和一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
*/
/**
与 15-三数之和 一样
先进行排序
a=nums[i] 从 nums[0] - nums[-1] 逐个取。
b 从 i+1 向后取
c 从 最后一位向前取
整个过程中始终记录最小距离，和三元组之和
*/


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
		int ret = 0;
		int dist = 0;
		if (nums.size() < 3) {
			return ret;
		}
		sort(nums.begin(), nums.end());
		ret = nums[0] + nums[1] + nums[2];
		dist = abs(ret - target);
		for (size_t i = 0; i < nums.size() - 2; ++i) {
			int a = nums[i];
			int lb = i + 1;
			int rb = nums.size() - 1;
			while (lb < rb) {
				int b = nums[lb];
				int c = nums[rb];
				int s = a + b + c;
				if (s == target) {
					return s;
				} else if (s < target) {
					lb ++;
				} else {
					rb --;
				}
				if (abs(s - target) < dist) {
					dist = abs(s - target);
					ret = s;
				}
			}
		}
		return ret;
    }
};

int main() {
	// vector<int> nums{-1, 2, 1, -4};
	// vector<int> nums{0, 2, 1, -3};  // -3, 0, 1, 2
	vector<int> nums{6,-18,-20,-7,-15,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10};
	int target = -52; //1;
	Solution solution;
	int res = solution.threeSumClosest(nums, target);
	cout << res << endl;
	return 0;
}
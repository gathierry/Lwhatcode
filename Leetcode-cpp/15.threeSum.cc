/**
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
/**
暴力法时间复杂度 O(n3)

可以先排序 O(nlogn)
之后依次从低到高取一个值 a，在 a 右边的子数组中，b 从左向右取，c从右向左取，直到相遇

a 不取重复的值，a > 0 时直接结束

b 和 c 也不取重复的值

时间复杂度 O(n2)

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
		vector<vector<int>> ret;
		if (nums.size() < 3) {
			return ret;
		}
		sort(nums.begin(), nums.end());
		for (size_t i = 0; i < nums.size() - 2; ++i) {
			int a = nums[i];
			if (a > 0) {
				break;
			}
			if (i > 0 && nums[i-1] == nums[i]) {
				continue;
			}
			int lb = i + 1;
			int rb = nums.size() - 1;
			while (lb < rb) {
				int b = nums[lb];
				int c = nums[rb];
				int s = a + b + c;
				if (s == 0) {
					vector<int> one_res{a, b, c};
					ret.push_back(one_res);
					lb ++;
					rb --;
					while (nums[lb] == b && lb < rb) {
						lb ++;
					}
					while (nums[rb] == c && lb < rb) {
						rb --;
					}
				} else if (s < 0) {
					lb ++;
					while (nums[lb] == b && lb < rb) {
						lb ++;
					}
				} else {
					rb --;
					while (nums[rb] == c && lb < rb) {
						rb --;
					}
				}
			}
		}
		return ret;
    }
};


int main() {
	// vector<int> nums{-1, 0, 1, 2, -1, -4};
	vector<int> nums{-2, 0, 0, 2, 2};
	Solution solution;
	vector<vector<int>> res = solution.threeSum(nums);
	for (size_t i = 0; i < res.size(); ++i) {
		for (size_t j = 0; j < res[i].size(); ++j) {
			cout << res[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}
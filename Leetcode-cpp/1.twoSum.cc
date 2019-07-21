/**
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
*/

/**
解法一：
暴力解法两两配对，时间复杂度 O(N^2)

解法二：
先排序，再前后加逼，时间复杂度 O(nlogn)
注意要记录原始的 index

解法三：
对于 target=t, nums=[n_0, n_1, ..., n_i]
遍历 nums:n_j，同时构造哈希表 d={t-n_0: 0, t-n_1: 1, ..., t-n_j: j}
如果遇到 n_i 在 d 中存在，说明 t-n_j = n_i, 那么输出 d[t-n_i], j
注意，为了避免重复利用同一个元素，需要在判断 n_i in d 之后，再将 t-n_i 放入 d
时间复杂度 O(n), 空间复杂度 O(n)
*/

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
		unordered_map<int, int> d;
		for (size_t j = 0; j < nums.size(); ++j) {
			if (d.find(nums[j]) != d.end()) {
				res.push_back(j);
				res.push_back(d[nums[j]]);
				return res;
			}
			d[target - nums[j]] = j;
		}
		return res;
    }
};

int main() {
	vector<int> nums{ 3, 2, 4};//{ 7, 2, 11, 15 };
	int target = 6; //9;
	Solution s;
	vector<int> res = s.twoSum(nums, target);
	for (auto x : res) {
		cout << x << " ";
	}
	return 0;
}
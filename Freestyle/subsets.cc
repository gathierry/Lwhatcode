/*
Given a set of distinct integers, return all possible subsets.

Example

Example 1:
Input: [0]
Output:
[
  [],
  [0]
]
Example 2:

Input: [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Challenge
Can you do it in both recursively and iteratively?

Notice
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution 
{
public:
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> subsets(vector<int> &nums) 
	{
        // write your code here
		vector<vector<int>> res;
		res.push_back(nums);
		res.push_back(nums);
		return res;
    }
};

void printIntVector(vector<int> v)
{
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i] << " ";
	}
	cout << endl;
}

int main()
{
	Solution s;
	vector<int> nums = {1,2,3};
	vector<vector<int>> res = s.subsets(nums);
	for (int i = 0; i < res.size(); ++i) {
		printIntVector(res[i]);
	}
}
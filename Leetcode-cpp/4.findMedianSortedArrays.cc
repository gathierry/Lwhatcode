/**
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
*/

/**
这道题可以转化成找第 N 个元素
设 nums1, nums2 长度分别为 l1, l2, l=l1+l2
若 l 是奇数，中位数是第 (l-1)/2 = int(l/2) 个数（从 0 开始）
若 l 是偶数，中位数是第 l/2 个数和 l/2-1 个数的平均数。

所以两个数组只要合计扔掉 r=l-(N+1) 个最大的数字后，剩下最大的数字就是第 N 个元素
每轮迭代 nums1 扔 r1 = r/2 个 或者 nums2 扔 r2 = r - r1 个
这里r_i 的范围，至少扔 1 个，最多全扔

那么我们来看 nums1 最后 r1 个数 和 nums2 最后 r2 个数谁的开头更大
开头大的将被扔掉，另一个则保持不变
形成的两个新的数组被重新放入递归函数

直到 l 长度等于 N + 1，取两个数组各自最后元素中较大的一个
或
两个数组中一个为空，取非空数组第 N 个元素
*/


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
	
	int findNthSortedArray(vector<int>& nums1, vector<int>& nums2, int l1, int l2, int n) {
		if (l1 == 0 && l2 > 0) {
			return nums2[n];
		}
		if (l1 > 0 && l2 == 0) {
			return nums1[n];
		}
		if (l1 + l2 == n + 1) {
			return max(nums1[l1-1], nums2[l2-1]);
		}
		int r = l1 + l2 - (n + 1); // element number to reject
		int r1 = max(1, min(r / 2, l1));
		int r2 = max(1, min(r - r1, l2));
		int i = l1 - r1;
		int j = l2 - r2;
		if (nums1[i] > nums2[j]) {
			l1 = i;
		} else if (nums1[i] < nums2[j]) {
			l2 = j;
		} else {
			l1 = i; // or l2 = j
		}
		return findNthSortedArray(nums1, nums2, l1, l2, n);
		
	}
	
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int l1 = nums1.size();
		int l2 = nums2.size();
		bool isOdd = ((l1 + l2) % 2 == 1);
		if (isOdd) {
			int med = findNthSortedArray(nums1, nums2, l1, l2, (l1 + l2) / 2);
			return static_cast<double>(med);
		} else {
			int med1 = findNthSortedArray(nums1, nums2, l1, l2, (l1 + l2) / 2 - 1);
			int med2 = findNthSortedArray(nums1, nums2, l1, l2, (l1 + l2) / 2);
			return static_cast<double>(med1 + med2) / 2.0;
		}
    }
};

int main() {
	// vector<int> nums1{ 1, 3};
	// vector<int> nums2{ 2};
	//
	// vector<int> nums1{ 1, 3, 4};
	// vector<int> nums2{ 2, 5};
	//
	// vector<int> nums1{ 1, 3, 5};
	// vector<int> nums2{ 2, 4, 6};
	//
	vector<int> nums1{ 1, 3, 5};
	vector<int> nums2{ 2, 3, 3, 6};
	//
	// vector<int> nums1{ 1, 3, 5};
	// vector<int> nums2{};
	//
	// vector<int> nums1{};
	// vector<int> nums2{ 2, 4};
	
	Solution s;
	double median = s.findMedianSortedArrays(nums1, nums2);
	cout << median << endl;
	
	
	return 0;
}

/*
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]
B=[2,4,5,6]
return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
*/
/*

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        // write your code here
		int la = A.size();
		int lb = B.size();
		vector<int> C;
		int ia = 0;
		int ib = 0;
		while (ia < la && ib < lb) {
			if (A[ia] <= B[ib]) {
				C.push_back(A[ia]);
				ia ++;
			} else {
				C.push_back(B[ib]);
				ib ++;
			}
		}
		if (ia < la) {
			for (int i = ia; i < la; i ++) {
				C.push_back(A[i]);
			}
		}
		if (ib < lb) {
			for (int i = ib; i < lb; i ++) {
				C.push_back(B[i]);
			}
		}
		return C;
    }
};

int main()
{
	Solution s;
	static const int a[] = {1,2,3,4};
	static const int b[] = {2,4,5,6};
	vector<int> A (a, a + sizeof(a) / sizeof(a[0]));
	vector<int> B (b, b + sizeof(b) / sizeof(b[0]));
	vector<int> v = s.mergeSortedArray(A, B);
	for (int i = 0; i < v.size(); ++i) {
		printf("%d, ", v[i]);
	}
	return 0;
}
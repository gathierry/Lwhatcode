/*
Write an algorithm which computes the number of trailing zeros in n factorial.

Example
11! = 39916800, so the out should be 2

Challenge
O(log N) time
*/
/*
搜索1~n中因数有5的个数（有2的个数一定大于等于有5的个数）
结果是 n//5 + n//25 + n//125 + ...
*/


#include <iostream>

class Solution {
public:
    /*
     * @param n: A long integer
     * @return: An integer, denote the number of trailing zeros in n!
     */
    long long trailingZeros(long long n) {
        // write your code here, try to do it without arithmetic operators.
		long long f = 5;
		long long s = 0;
		while (f <= n) {
			s += (n / f);
			f *= 5;
		}
		return s;
    }
};

int main()
{
	using namespace std;
	Solution s;
	int z = s.trailingZeros(5555550000000);
	cout << z << endl;
	return 0;
}
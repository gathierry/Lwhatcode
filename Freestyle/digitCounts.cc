/*
Count the number of k's between 0 and n. k can be 0 - 9.

Example
if n = 12, k = 1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
we have FIVE 1's (1, 10, 11, 12)
*/
/*
假设m位数 a_m a_{m-1} ... a2 a1
拆解成 0 ~ a_{m-1} ... a2 a1 和 a_{m-1} ... a2 a1 + 1 ~ a_m a_{m-1} ... a2 a1
第一部分可以通过递归方式求解，终止条件是位数为 1
第二部分
	k != 0 时
		计算前 m-1 位可以有多少个 k，排列组合计算得：s=(m-1)*10^(m-2)
		如果 a_m < k，a_m * s
		如果 a_m = k, a_m * s +  a_{m-1} ... a2 a1 + 1
		如果 a_m > k, a_m * s + 10^(m-1)
	k == 0 时
		计算前 m-1 位可以有多少个 k，排列组合计算得：s=(m-1)*10^(m-2) - (10^(m-1) - a_{m-1} ... a2 a1 - 1)
		因为 a_m 一定 > k, a_m * s

一个数字 n 有 logn 位，因此时间复杂度是 O(logn)
*/

#include <iostream>
#include <string>
#include <cmath>

class Solution {
public:
    /**
     * @param k: An integer
     * @param n: An integer
     * @return: An integer denote the count of digit k in 1..n
     */
    int digitCounts(int k, int n) {
        // write your code here
		std::string str = std::to_string(n);
		int m = str.size();
		if (m==1) {
			return n >= k ? 1 : 0;
		}
		int am = n / std::pow(10.0, (m-1));
		int r = n - am*std::pow(10.0, (m-1));
		int s = (m-1) * std::pow(10.0, (m-2));
		if (k == 0) {
			s -= (std::pow(10.0, m-1) - r - 1);
		}
		if (am < k) {
			s = am * s;
		} else if (am == k) {
			s = am * s + r + 1;
		} else {
			s = k == 0 ? am * s : am * s + std::pow(10.0, (m-1));
		}
		printf("%d, %d, %d \n", r, am, s);
		return s + digitCounts(k, r);
    }
};

int main()
{
	using namespace std;
	Solution s;
	int z = s.digitCounts(3, 12345);
	cout << z << endl;
	return 0;
}
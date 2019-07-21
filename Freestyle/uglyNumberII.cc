/*
Ugly number is a number that only have factors 2, 3 and 5.
Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Example
If n=9, return 10.

Challenge
O(n log n) or O(n) time.

Notice
Note that 1 is typically treated as an ugly number.
*/
/*
构建三个队列
1, 2, 2*2, 2*3, ...
1. 3, 3*2, 3*3, ...
1, 5, 5*2, 5*3, ...
每次从三个队列排头取出最小的一个（相等时都取出），几位 k，将结果乘以丑数放入队列最后
*/

#include <iostream>
#include <queue>
#include <vector>

class Solution {
public:
    /**
     * @param n: An integer
     * @return: the nth prime number as description.
     */
    int nthUglyNumber(int n) {
        // write your code here
		using namespace std;
		queue<int> q2;
		q2.push(1);  // 1 is the first ugly number
		queue<int> q3;
		q3.push(1);
		queue<int> q5;
		q5.push(1);
		vector<queue<int> > qs;
		qs.push_back(q2);
		qs.push_back(q3);
		qs.push_back(q5);
		int minV = 0;
		int i = 0;
		while (i < n) {
			minV = min(min(q2.front(), q3.front()), q5.front());
			if (q2.front() == minV) q2.pop();
			if (q3.front() == minV) q3.pop();
			if (q5.front() == minV) q5.pop();
			q2.push(minV*2);
			q3.push(minV*3);
			q5.push(minV*5);
			i ++;
		}
		return minV;
    }
};

int main()
{
	using namespace std;
	Solution s;
	int n = s.nthUglyNumber(9);
	cout << n << endl;
	return 0;
}
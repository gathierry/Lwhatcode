/*
Write a function that add two numbers A and B.

Example
Given a=1 and b=2 return 3.

Challenge
Of course you can just return a + b to get accepted. But Can you challenge not do it like that?(You should not use + or any arithmetic operators.)

Clarification

Are a and b both 32-bit integers?
Yes.

Can I use bit operation?
Sure you can.
*/

/*
可以用位运算
c = a & b 表示需要进位的位
d = a ^ b 表示不需要进位的位
c << 后再加 d

*/

#include <iostream>

class Solution {
public:
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b 
     */
    int aplusb(int a, int b) {
        // write your code here
		int c = a & b;
		int d = a ^ b;
		if (c != 0) {
			return aplusb(d, c<<1);
		} else {
			return d;
		}
    }
};

int main()
{
	using namespace std;
	Solution s;
	int sum = s.aplusb(1, 2);
	cout << sum << endl;
	return 0;
}
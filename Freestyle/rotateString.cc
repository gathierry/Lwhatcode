/*
Given a string and an offset, rotate string by offset. (rotate from left to right)

Example
Given "abcdefg".
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

Challenge
Rotate in-place with O(1) extra memory.
*/
/*
为了在 O(n) 时间内完成
方法一：
在字符串后面接一段 str[:l-offset]，之后取子字符串
但是空间复杂度也为 O(n)
方法二：
设 A.T 是 A 的逆序排列
有 (A.T B.T).T = BA
*/

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    /**
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    void rotateString(string &str, int offset) {
        // write your code here
		int len = str.size();
		if (len == 0) {
			return;
		}
		offset = offset % len;
		
		reverseString(str, 0, len-1-offset);
		reverseString(str, len-offset, len-1);
		reverseString(str, 0, len-1);
    }
	
	void reverseString(string &str, int start, int end) {
		while (start < end) {
			char tmp = str[start];
			str[start] = str[end];
			str[end] = tmp;
			start ++;
			end --;
		}
	}
};

int main()
{
	Solution s;
	string str = "abcdefg";
	int offset = 2;
	s.rotateString(str, offset);
	cout << str << endl;
	return 0;
}
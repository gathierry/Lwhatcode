/*
Given number n. Print number from 1 to n. But:
when number is divided by 3, print "fizz".
when number is divided by 5, print "buzz".
when number is divided by both 3 and 5, print "fizz buzz".

Example
If n = 15, you should return:
[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]

Challenge
Can you do it with only one if statement?
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * @param n: An integer
     * @return: A list of strings.
     */
    vector<string> fizzBuzz(int n) {
		vector<string> res;
        for (int i = 1; i <= n; ++i) {
			string str = "";
			bool fizz = (i%3 == 0);
			bool buzz = (i%5 == 0);
        	if (fizz && !buzz) {
        		str = "fizz";
        	} else if (!fizz && buzz) {
        		str = "buzz";
        	} else if (fizz && buzz) {
        		str = "fizz buzz";
        	} else {
        		str = to_string(i);
        	}
			res.push_back(str);
        }
		return res;
    }
};

int main()
{
	Solution s;
	static const int n = 15;
	vector<string> v = s.fizzBuzz(n);
	for (int i = 0; i < v.size(); ++i) {
		cout << v[i] << endl;
	}
	return 0;
}
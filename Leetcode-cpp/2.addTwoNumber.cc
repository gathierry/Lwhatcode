/**
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
*/

/**
两个链表分别是从低位到高位，
a1 -> a2 -> a3
b1 -> b2 -> b3
临时变量 t 表示进位 0 或 1
*/

#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode *l1, ListNode *l2) {
		ListNode *head = new ListNode(0);
		ListNode *node = head;
		int t = 0;
		while (l1 || l2) {
			if (l1) {
				node->val += l1->val;
				l1 = l1->next;
			}
			if (l2) {
				node->val += l2->val;
				l2 = l2->next;
			}
			t = node->val / 10;
			node->val = node->val%10;
			if (l1 || l2 || t) {
				node->next = new ListNode(t);
				node = node->next;
			}
		}
        return head;
    }
};

int main() {
	ListNode *l1_0 = new ListNode(2);
	ListNode *l1_1 = new ListNode(4);
	ListNode *l1_2 = new ListNode(3);
	l1_0->next = l1_1;
	l1_1->next = l1_2;
	ListNode *l2_0 = new ListNode(5);
	ListNode *l2_1 = new ListNode(6);
	ListNode *l2_2 = new ListNode(4);
	l2_0->next = l2_1;
	l2_1->next = l2_2;
	
	Solution s;
	ListNode *l3 = s.addTwoNumbers(l1_0, l2_0);
	while (l3) {
		cout << l3->val << " ";
		l3 = l3->next;
	}
	
	
	return 0;
}
"""
Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
Given A=[1,2,3] and B=[4,5], the median is 3.

Challenge
The overall run time complexity should be O(log (m+n)).
"""
"""
将问题泛化成寻找第k大的数
如果 A B 长度都大于 k/2
    对比 A[k/2-1] B[k/2-1]
    如果 A[k/2-1] > B[k/2-1]
        那么 B[0] 到 B[k/2-1] 都不可能是要找的数
    如果 A[k/2-1] < B[k/2-1]
        那么 A[0] 到 A[k/2-1] 都不可能是要找的数
    如果 A[k/2-1] = B[k/2-1]
        那么 A[k/2-1] 是要找的数

如果 A B 有一个长度不足 k/2
比如 B 的长度 l < k/2
那么对比 B[l-1] 和 A[k/2-l-l]    
        
"""


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        la = len(A)
        lb = len(B)
        if (la+lb) % 2 == 1:
            return self.findKthElement(A, B, (la+lb+1)//2)
        else:
            return float(self.findKthElement(A, B, (la+lb)//2) + self.findKthElement(A, B, (la+lb)//2+1)) / 2.0
        
    def findKthElement(self, A, B, k):
        """
        Assuming len(A) <= len(B)
        """
        if len(A) > len(B):
            return self.findKthElement(B, A, k)
        if len(A) == 0:
            return B[k-1]
        if (k==1):
            return min(A[0], B[0])
        
        ia = min(k//2-1, len(A)-1)
        ib = k - 2 - ia
        if A[ia] > B[ib]:
            if len(B) - 1 == ib:
                return self.findKthElement(A, [], k-ia-1)
            return self.findKthElement(A, B[ib+1:], k-ib-1)
        elif A[ia] < B[ib]:
            if len(A) - 1 == ia:
                return self.findKthElement([], B, k-ia-1)
            return self.findKthElement(A[ia+1:], B, k-ia-1)
        else:
            return A[ia]
        
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,2,3,4,5,6], [2,3,4,5]))
    print(s.findMedianSortedArrays([1,2,3], [4,5]))
    print(s.findMedianSortedArrays([], [4,5]))
    print(s.findMedianSortedArrays([3], [4]))
        
        
        
        
        
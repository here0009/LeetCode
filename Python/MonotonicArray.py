"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true

Example 2:

Input: [6,5,4,4]
Output: true

Example 3:

Input: [1,3,2]
Output: false

Example 4:

Input: [1,2,4,5]
Output: true

Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        len_A = len(A)
        if len_A == 1 or len_A == 2:
            return True
        
        flag = 0
        for i in range(1, len_A):
            # print(flag)
            if flag == 0:
                if A[i]-A[i-1] > 0:
                    flag = 1 #increasing
                if A[i]-A[i-1] < 0:
                    flag = -1 #decreaing
            if flag == 1 and A[i]-A[i-1] < 0:
                return False
            if flag == -1 and A[i]-A[i-1] > 0:
                return False

        return True

s = Solution()

test = [1,2,2,3]
print(s.isMonotonic(test))

test_list = [[6,5,4,4],[1,3,2],[1,2,4,5],[1,1,1],]
for test in test_list:
    print(s.isMonotonic(test))


test = [5,3,2,4,1]
print(s.isMonotonic(test))

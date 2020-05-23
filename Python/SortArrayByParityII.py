"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
"""
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1
        break_flag = False
        while even <= len(A)-1 and odd <= len(A)-1:
            while A[even]%2 == 0:
                even += 2
                if even > len(A)-1:
                    break_flag = True
                    break
            while A[odd]%2 == 1:
                odd += 2
                if odd > len(A)-1:
                    break_flag = True
                    break
            if not break_flag:
                A[even], A[odd] = A[odd], A[even]
                even += 2
                odd += 2
        return A

s = Solution()
A = [4,2,5,7]
print(s.sortArrayByParityII(A))
A = [2,3]
print(s.sortArrayByParityII(A))
A = [3,2]
print(s.sortArrayByParityII(A))
# A = [2,3,2,3]
# print(s.sortArrayByParityII(A))
# A = [3,2,3,2]
# print(s.sortArrayByParityII(A))
A = [2,3,1,1,4,0,0,4,3,3]
print(s.sortArrayByParityII(A))

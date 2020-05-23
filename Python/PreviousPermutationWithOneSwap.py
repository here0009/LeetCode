"""
Given an array A of positive integers (not necessarily distinct), return the lexicographically largest permutation that is smaller than A, that can be made with one swap (A swap exchanges the positions of two numbers A[i] and A[j]).  If it cannot be done, then return the same array.

 

Example 1:

Input: [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
Example 4:

Input: [3,1,1,3]
Output: [1,3,1,3]
Explanation: Swapping 1 and 3.
 

Note:

1 <= A.length <= 10000
1 <= A[i] <= 10000
"""
class Solution_1:
    def prevPermOpt1(self, A):
        """
        exchange the last anti-order
        """
        pre = 0
        exchange_a = exchange_b = pre
        anti_order_flag = False
        for i in range(1,len(A)):
            if A[pre] > A[i]:
                exchange_a, exchange_b = pre, i
                anti_order_flag = True
            if anti_order_flag and A[exchange_b] < A[i] and A[i] < A[exchange_a]:
                exchange_b = i
            pre = i
            # print(A[exchange_a], A[exchange_b])
        A[exchange_a], A[exchange_b] = A[exchange_b], A[exchange_a]
        return A

class Solution:
    def prevPermOpt1(self, A):
        """
        exchange the last anti-order, move from right to left, if ther is an anti-order then i-1 is the left_pointer, i is the right_pointer
        then move from right_pointer to right, if it is larger than current right_pointer and small than left_pointer, then it is the new right_pointer
        """

        for i in range(len(A)-1, 0, -1):
            if A[i] < A[i-1]:
                left_pointer = i-1
                right_pointer = i
                break
        else:
            return A

        for j in range(right_pointer+1, len(A)):
            if A[j] > A[right_pointer] and A[j] < A[left_pointer]:
                right_pointer = j
        A[left_pointer], A[right_pointer] = A[right_pointer], A[left_pointer]

        return A

s = Solution()
A = [3,2,1]
print(s.prevPermOpt1(A))

A = [1,1,5]
print(s.prevPermOpt1(A))

A = [1,9,4,6,7]
print(s.prevPermOpt1(A))

A = [3,1,1,3]
print(s.prevPermOpt1(A))

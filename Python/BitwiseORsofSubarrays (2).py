"""
We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

 

Example 1:

Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.

Example 2:

Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.

Example 3:

Input: [1,2,4]
Output: 6
Explanation: 
The possible results are 1, 2, 3, 4, 6, and 7.
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 10^9
"""
class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res_set = set()
        len_A = len(A)
        if len_A == 1:
            return 1
        for i in range(len_A):
            tmp_num = A[i]
            if tmp_num not in res_set:
                res_set.add(tmp_num)
            for j in range(i+1, len_A):
                tmp_num = tmp_num | A[j]
                if tmp_num not in res_set:
                    res_set.add(tmp_num)
        return len(res_set)

s = Solution()
# test_list = [[0], [1,1,2], [1,2,4]]
# for test in test_list:
#     print(s.subarrayBitwiseORs(test))

test = [39,19,30,56,79,50,19,70,30]
print(s.subarrayBitwiseORs(test))

"""
Thoughts:
Use prime number in len(A) to merge the list, and add bitwise value
"""
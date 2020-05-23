"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.
"""
class Solution:
    def partitionDisjoint(self, A) -> int:
        res_index = 0
        max_num = A[0]
        next_max = A[0]
        for i in range(1,len(A)):
            # print(A[i], max_num, next_max, A[res_index])
            if A[i] < max_num:
                max_num = next_max
                res_index = i
            else:
                next_max = max(A[i], next_max)
        return res_index+1


S = Solution()
A = [5,0,3,8,6]
print(S.partitionDisjoint(A))
A = [1,1,1,0,6,12]
print(S.partitionDisjoint(A))
A = [24,11,49,80,63,8,61,22,73,85]
print(S.partitionDisjoint(A))
# Output
# 8
# Expected
# 9
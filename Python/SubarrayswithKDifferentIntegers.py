"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""
class Solution:
    """
    the input is [1,2,1,3,4], K is 3
    1. find the longest_subarray that got K elments, that's [1,2,1,3]
    2. then find the subarraies of longest_subarray that meet the requirements, they are [1,2,1,3],[2,1,3]
    3. then sliding the window, find another longest_subarray
    find the res
    """
    def subarraysWithKDistinct(self, A, K: int) -> int:
        res = 0
        num_pos = 

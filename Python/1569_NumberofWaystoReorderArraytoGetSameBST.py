"""
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

 

Example 1:



Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:



Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:



Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
Example 4:



Input: nums = [3,1,2,5,4,6]
Output: 19
Example 5:

Input: nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
Output: 216212978
Explanation: The number of ways to reorder nums to get the same BST is 3216212999. Taking this number modulo 10^9 + 7 gives 216212978.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
"""


from functools import lru_cache
class Solution:
    """
    we can solve the problem in 4 steps
    1. split the tree into left subtree and right subtree. the root is nums[0]
    2. find the ways of reorder left subtree and rightsubtree
    3. find the ways to combine right subtree and left subtree(the order inside left subtree and right subtree does not matter now)
    4. recurse the steps above.
    """
    def numOfWays(self, nums) -> int:
        @lru_cache(None)
        def fact(k):
            """
            return the factorial number of k
            """
            res = 1
            while k > 1:
                res *= k
                k -= 1
            return res

        def comb(m, n):
            """
            choose n positions out of m positions the order does not matter
            """
            if m == 0 or n == 0:
                return 1
            return fact(m) //(fact(n)*fact(m-n))

        def ways(vals):
            if len(vals) <= 1:
                return 1
            left = [v for v in vals if v < vals[0]]
            right = [v for v in vals if v > vals[0]]
            return ways(left) * ways(right) * comb(len(left)+len(right), len(left)) % M

        M = 10**9 + 7
        return (ways(nums)-1)% M 

S = Solution()
nums = [2,1,3]
print(S.numOfWays(nums))
nums = [3,4,5,1,2]
print(S.numOfWays(nums))
nums = [1,2,3]
print(S.numOfWays(nums))
nums = [3,1,2,5,4,6]
print(S.numOfWays(nums))
nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
print(S.numOfWays(nums))

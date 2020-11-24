"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
"""


from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        find the 1st pattern of 13, then update to get 3 max value we encounter, then find 2
        """
        length = len(nums)
        i = 0
        while i+1 < length and nums[i] >= nums[i+1]: 
            i += 1
        # nums[i] < nums[i+1]
        if i+1 >= length:
            return False
        min_v, max_v = nums[i], nums[i+1]
        for j in range(i+1, length):
            max_v = max(max_v, nums[j])
            if nums[j] < max_v:
                return True
        return False

from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        nums_index = sorted([(v, i) for i,v in enumerate(nums)])
        for i in range(2, length):
            v1, i1 = nums_index[i-2]
            v2, i2 = nums_index[i-1]
            v3, i3 = nums_index[i]
            if v1 < v2 < v3 and i1 < i3 < i2:
                return True
        return False
            
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        def insert(node, num):
            if not node:
                return Node(num)
            if num < node.val:
                node.left = insert(node.left, num)
            elif num > node.val:
                if node.right and num < node.right.val:
                    self.res = True
                node.right = insert(node.right, num)
            return node

        root = Node(nums[0])
        self.res = False
        for num in nums[1:]:
            insert(root, num)
            if self.res:
                return True
        return False


S = Solution()
nums = [1,2,3,4]
print(S.find132pattern(nums))
nums = [3,1,4,2]
print(S.find132pattern(nums))
nums = [-1,3,2,0]
print(S.find132pattern(nums))
nums = [1,0,1,-4,-3]
print(S.find132pattern(nums))
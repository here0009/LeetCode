"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.

It's guaranteed that the given list represents a valid connected binary tree.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation: 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
 

Example 2:

Input: [113, 221]
Output: 4
Explanation: 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import Counter
class Solution:
    def pathSum(self, nums) -> int:
        counts = Counter()
        res = 0
        for num in nums[::-1]:
            d, p, v = [int(s) for s in list(str(num))]
            if (d,p) not in counts:
                counts[(d,p)] = 1
            res += counts[(d,p)]*v
            counts[(d-1,(p+1)//2)] += counts[(d,p)]
            # print(counts)
        return res

S = Solution()
nums = [113, 215, 221]
print(S.pathSum(nums))
nums = [113, 221]
print(S.pathSum(nums))
nums = [113,229,349,470,485]
print(S.pathSum(nums))
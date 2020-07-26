"""
Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

 

Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
Example 4:

Input: root = [100], distance = 1
Output: 0
Example 5:

Input: root = [1,1,1], distance = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 2^10].
Each node's value is between [1, 100].
1 <= distance <= 10
"""


# Definition for a binary tree node.
from LeetCode import construcTree
from LeetCode import printBinaryTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return None
            res = Counter()
            left = dfs(node.left)
            right = dfs(node.right)
            if not left and not right:
                return Counter({1:1})
            if left:
                for li, lv in left.items():
                    res[li + 1] += lv
            if right:
                for ri, rv in right.items():
                    res[ri + 1] += rv
            if left and right:
                for li, lv in left.items():
                    for ri, rv in right.items():
                        if li + ri <= distance:
                            self.res += lv*rv
            # print()
            # print(node.val,'res',res)
            return res

        self.res = 0
        dfs(root)
        return self.res


S = Solution()
root = [78,15,81,73,98,36,None,30,None,63,32]
distance = 6
root = construcTree(root)
printBinaryTree(root)
print(S.countPairs(root, distance))
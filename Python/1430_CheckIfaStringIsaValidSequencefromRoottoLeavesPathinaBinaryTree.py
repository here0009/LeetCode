"""
Given a binary tree where each path going from the root to any leaf form a valid sequence, check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.

 

Example 1:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
Output: true
Explanation: 
The path 0 -> 1 -> 0 -> 1 is a valid sequence (green color in the figure). 
Other valid sequences are: 
0 -> 1 -> 1 -> 0 
0 -> 0 -> 0
Example 2:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
Output: false 
Explanation: The path 0 -> 0 -> 1 does not exist, therefore it is not even a sequence.
Example 3:



Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
Output: false
Explanation: The path 0 -> 1 -> 1 is a sequence, but it is not a valid sequence.
 

Constraints:

1 <= arr.length <= 5000
0 <= arr[i] <= 9
Each node's value is between [0 - 9].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        def dfs(node, index):
            if index == length and node is None:
                return True
            if node is None or index >= length or node.val != arr[index]:
                return False
            left = dfs(node.left, index+1)
            right = dfs(node.right, index+1)
            if left and right:
                self.res = True
            return left or right

        self.res = False
        length = len(arr)
        dfs(root, 0)
        return self.res


class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        def dfs(node, index):
            if node is None or index >= length or node.val != arr[index]:
                return False
            if index == length-1 and not node.left and not node.right:
                return True
            return dfs(node.left, index+1) or dfs(node.right, index+1)
            
        length = len(arr)
        return dfs(root, 0)

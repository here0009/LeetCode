"""
Given a non-empty binary tree, return the average value of the nodes on each level_num in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level_num 0 is 3,  on level_num 1 is 14.5, and on level_num 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def __init(self):
    #     self.level_dict = dict()
    #     self.level_num = 0

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        global level_dict, level_num
        level_dict = dict()
        level_num = 0
        self.traverseBST(root, level_num, level_dict)

        return [sum(level_dict[level])/len(level_dict[level]) for level in sorted(level_dict.keys())]


    def traverseBST(self, root, level_num, level_dict):

        if level_num not in level_dict:
            level_dict[level_num] = [root.val]
        else:
            level_dict[level_num].append(root.val)
        if root.left:
            self.traverseBST(root.left, level_num+1, level_dict)
        if root.right:
            self.traverseBST(root.right, level_num+1, level_dict)
        return


"""
The solution below using breadth first search, append the value of each level to a list, then return the list
"""
class Solution_1:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        q = [root]
        while q:
            new_q = []
            total = 0
            size = len(q)
            for node in q:
                total += node.val
                if node.left: new_q.append(node.left)
                if node.right: new_q.append(node.right)
            res.append(total / size)
            q = new_q
        return res
"""
Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.
 

Example 1:



Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:



Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:



Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 10^4]
Total calls of find() is between [1, 10^4]
0 <= target <= 10^6
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from bisect import bisect_left
class FindElements:

    def __init__(self, root: TreeNode):
        def recover(root,val):
            if not root:
                return
            root.val = val
            recover(root.left, val*2+1)
            recover(root.right, val*2+2)
        recover(root, 0)
        self.root = root
        self.nums = []
        nodes = [root]
        while len(nodes)>0:
            tmp_nodes = []
            for node in nodes:
                self.nums.append(node.val)
                if node.left:
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_nodes.append(node.right)
            nodes = tmp_nodes
        self.len = len(self.nums)
        print(self.root.val)
        print(self.root.right.val)

    def find(self, target: int) -> bool:
        index = bisect_left(self.nums, target)
        if index == self.len or self.nums[index] != target:
            return False
        else:
            return True

# Your FindElements object will be instantiated and called as such:
obj = FindElements(root)
param_1 = obj.find(target)
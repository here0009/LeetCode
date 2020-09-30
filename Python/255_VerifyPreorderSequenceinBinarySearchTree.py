"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def verifyPreorder(self, preorder) -> bool:
        """
        TLE
        """
        if len(preorder) < 2:
            return True
        v = preorder[0]
        index = 1
        while index < len(preorder) and preorder[index] < v:
            index += 1
        for i in range(index, len(preorder)): # if preorder is a preorder traverse of bst, all vals in preorder[index:] should larger than v
            if preorder[i] < v:
                return False
        return self.verifyPreorder(preorder[1:index]) and self.verifyPreorder(preorder[index:])

class Solution:
    def verifyPreorder(self, preorder) -> bool:
        """
        使用stack维持一个递减序列， 
        遇到比stack[-1]大的数（mid），将数pop到inorder中（left）
        如果原序列为前序遍历，则inorder + stack应该是排序好的数
        """
        inorder = []
        stack = []
        for i in range(len(preorder)):
            while stack and preorder[i] > stack[-1]:
                inorder.append(stack.pop())
            stack.append(preorder[i])
        inorder += stack[::-1]
        # print(inorder)
        for i in range(1, len(inorder)):
            if inorder[i] < inorder[i-1]:
                return False
        return True

# 二叉搜索树的前序遍历有以下特点：

# 如果出现递减序列，则是左子树，否则是右子树；
# 右子树一定是递增的
# 综上，我们可以通俗理解为“总体递增，局部递减”。为了达到“总体递增的效果”，我们要保证递减序列的第一个元素小于递减结束后即将递增的那个元素。因此，我们我们使用new_min和栈，如果递减结束后，下一个元素小于递减序列的第一个元素，违背了“总体递增”，立即返回False。


class Solution:
    def verifyPreorder(self, preorder) -> bool:
        """
        preorder is: mid, left, right; so the min value will be visited 1st.
        """

        min_v = float('-inf')
        stack = []
        for i in range(len(preorder)):
            if preorder[i] < min_v:
                return False
            while stack and preorder[i] > stack[-1]:
                min_v = stack.pop()
            stack.append(preorder[i])
        return True

S = Solution()
preorder = [5,2,6,1,3]
print(S.verifyPreorder(preorder))
preorder = [5,2,1,3,6]
print(S.verifyPreorder(preorder))
preorder = [2,1]
print(S.verifyPreorder(preorder))
preorder = [2,3,1]
print(S.verifyPreorder(preorder))
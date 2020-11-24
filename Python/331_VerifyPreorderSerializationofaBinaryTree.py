"""
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \\   / \
 4   1  #  6
/ \\ / \\   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".

Example 1:

Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true
Example 2:

Input: "1,#"
Output: false
Example 3:

Input: "9,#,#,1"
Output: false
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        vals = preorder.split(',')
        print(vals)
        stack = []
        for v in vals:
            if v == '#':
                while len(stack) > 1 and stack[-1] == '#' and stack[-2] != '#':
                    stack.pop()
                    stack.pop()
            stack.append(v)
            # print(v, stack)
        return len(stack) == 1 and stack.pop() == '#'


S = Solution()
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
print(S.isValidSerialization(preorder))
preorder = "1,#"
print(S.isValidSerialization(preorder))
preorder = "9,#,#,1"
print(S.isValidSerialization(preorder))
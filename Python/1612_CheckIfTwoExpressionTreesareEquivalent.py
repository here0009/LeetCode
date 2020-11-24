"""
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (variables), and internal nodes (nodes with two children) correspond to the operators. In this problem, we only consider the '+' operator (i.e. addition).

You are given the roots of two binary expression trees, root1 and root2. Return true if the two binary expression trees are equivalent. Otherwise, return false.

Two binary expression trees are equivalent if they evaluate to the same value regardless of what the variables are set to.

Follow up: What will you change in your solution if the tree also supports the '-' operator (i.e. subtraction)?

 

Example 1:

Input: root1 = [x], root2 = [x]
Output: true
Example 2:



Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,b,c,a]
Output: true
Explaination: a + (b + c) == (b + c) + a
Example 3:



Input: root1 = [+,a,+,null,null,b,c], root2 = [+,+,b,d,a]
Output: false
Explaination: a + (b + c) != (b + d) + a
 

Constraints:

The number of nodes in both trees are equal, odd and, in the range [1, 4999].
Node.val is '+' or a lower-case English letter.
It's guaranteed that the tree given is a valid binary expression tree.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-if-two-expression-trees-are-equivalent
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import Counter
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def dfs(node, counts):
            if not node:
                return
            v = node.val
            if v != '+':
                counts[v] += 1
            dfs(node.left, counts)
            dfs(node.right, counts)

        counts1 = Counter()
        counts2 = Counter()
        dfs(root1, counts1)
        dfs(root2, counts2)
        lst1 = sorted([(k,v) for k, v in counts1.items()])
        lst2 = sorted([(k,v) for k, v in counts2.items()])
        return lst1 == lst2


from collections import Counter
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def dfs(node, counts):
            if not node:
                return
            v = node.val
            if v != '+':
                counts[v] += 1
            dfs(node.left, counts)
            dfs(node.right, counts)

        counts1 = Counter()
        counts2 = Counter()
        dfs(root1, counts1)
        dfs(root2, counts2)

        return counts1 == counts2

[+,a,+,null,null,b,c]
[+,+,b,c,a]
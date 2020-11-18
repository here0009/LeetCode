"""
A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with 2 children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

For each internal node with operator o, the infix expression that it represents is (A o B), where A is the expression the left subtree represents and B is the expression the right subtree represents.

You are given a string s, an infix expression containing operands, the operators described above, and parentheses '(' and ')'.

Return any valid binary expression tree, which its in-order traversal reproduces s after omitting the parenthesis from it (see examples below).

Please note that order of operations applies in s. That is, expressions in parentheses are evaluated first, and multiplication and division happen before addition and subtraction.

Operands must also appear in the same order in both s and the in-order traversal of the tree.

 

Example 1:



Input: s = "2-3/(5*2)+1"
Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is the same as s without the parenthesis. The tree also produces the correct result and its operands are in the same order as they appear in s.
The tree below is also a valid binary expression tree with the same inorder traversal as s:

The third tree below however is not valid. Although it produces the same result and is equivalent to the above trees, its inorder traversal doesn't produce s and its operands are not in the same order as s.

Example 2:



Input: s = "3*4-2*5"
Output: [-,*,*,3,4,2,5]
Explanation: The tree above is the only valid tree whose inorder traversal produces s.
Example 3:

Input: s = "1+2+3+4+5"
Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other valid trees.
 

Constraints:

1 <= s.length <= 105
s consists of digits and the characters '+', '-', '*', '/', '(', and ')'.
Operands in s are exactly 1 digit.
It is guaranteed that s is a valid expression.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/build-binary-expression-tree-from-infix-expression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> 'Node':
        """
        wrong answer
        """
        def toNode(string):
            if not string:
                return None

            if string[0] == '(' and string[-1] == ')':
                return toNode(string[1:-1])
            left, right = 0, len(string)-1
            if '(' in string:
                right = string.find('(')
            if ')' in string:
                left = string.rfind(')') + 1
            for sign in self.signs:
                if sign in string[left:]:
                    index = string.find(sign, left)
                elif sign in string[:right]:
                    index = string.find(sign)
                else:
                    continue
                left_node = toNode(string[:index])
                right_node = toNode(string[index+1:])
                return Node(string[index], left_node, right_node)
            return Node(string)

        self.signs = '+-*/'
        return toNode(s)

class Solution:
    def expTree(self, s: str) -> 'Node':
        def toNode(string):
            if not string:
                return None
            stack = []
            operands = []
            index, length, digits = 0, len(string), ''
            while index < length:
                c = string[index]
                if c == '(':
                    p = 0
                    p_index = index
                    while p_index < length:
                        if string[p_index] == '(':
                            p += 1
                        elif string[p_index] == ')':
                            p -= 1
                        if p == 0:
                            break
                        p_index += 1
                    stack.append(toNode(string[index+1:p_index]))
                    index = p_index
                elif c.isdigit():
                    digits += c
                else:
                    if digits:
                        stack.append(Node(digits))
                        digits = ''
                        if operands and operands[-1] in '*/':
                            q = stack.pop()
                            p = stack.pop()
                            stack.append(Node(operands.pop(), p, q))
                    if c in '+-*/':
                        operands.append(c)
                index += 1
            if digits:
                stack.append(Node(digits))

            while len(stack) > 1:
                q = stack.pop()
                p = stack.pop()
                stack.append(Node(operands.pop(), p, q))
            return stack.pop()

        return toNode(s)

S = Solution()
string = "2-3/(5*2)+1"
print(S.expTree(string))
# string = "3*4-2*5"
# print(S.expTree(string))
# string = "1+2+3+4+5"
# print(S.expTree(string))
# s = "(9*9-(9-7)*3)/(3*1)"
# print(S.expTree(string))


# 输入：
# "(9*9-(9-7)*3)/(3*1)"
# 输出：
# [-,*,*,9,9,/,1,null,null,null,null,-,(3,null,null,9,*,null,null,null,null,7),3]
# 预期结果：
# [/,-,*,*,*,3,1,9,9,-,3,null,null,null,null,null,null,null,null,9,7]
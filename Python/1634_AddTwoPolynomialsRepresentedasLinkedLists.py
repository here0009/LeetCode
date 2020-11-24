"""
A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

Each node has three attributes:

coefficient: an integer representing the number multiplier of the term. The coefficient of the term 9x4 is 9.
power: an integer representing the exponent. The power of the term 9x4 is 4.
next: a pointer to the next node in the list, or null if it is the last node of the list.
For example, the polynomial 5x3 + 4x - 7 is represented by the polynomial linked list illustrated below:



The polynomial linked list must be in its standard form: the polynomial must be in strictly descending order by its power value. Also, terms with a coefficient of 0 are omitted.

Given two polynomial linked list heads, poly1 and poly2, add the polynomials together and return the head of the sum of the polynomials.

PolyNode format:

The input/output format is as a list of n nodes, where each node is represented as its [coefficient, power]. For example, the polynomial 5x3 + 4x - 7 would be represented as: [[5,3],[4,1],[-7,0]].

 

Example 1:



Input: poly1 = [[1,1]], poly2 = [[1,0]]
Output: [[1,1],[1,0]]
Explanation: poly1 = x. poly2 = 1. The sum is x + 1.
Example 2:

Input: poly1 = [[2,2],[4,1],[3,0]], poly2 = [[3,2],[-4,1],[-1,0]]
Output: [[5,2],[2,0]]
Explanation: poly1 = 2x2 + 4x + 3. poly2 = 3x2 - 4x - 1. The sum is 5x2 + 2. Notice that we omit the "0x" term.
Example 3:

Input: poly1 = [[1,2]], poly2 = [[-1,2]]
Output: []
Explanation: The sum is 0. We return an empty list.
 

Constraints:

0 <= n <= 104
-109 <= PolyNode.coefficient <= 109
PolyNode.coefficient != 0
0 <= PolyNode.power <= 109
PolyNode.power > PolyNode.next.power

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-polynomials-represented-as-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

from collections import Counter
class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        def readPoly(poly):
            if not poly:
                return
            counts[poly.power] += poly.coefficient
            readPoly(poly.next)

        counts = Counter()
        readPoly(poly1)
        readPoly(poly2)
        keys = sorted([k for k in counts.keys() if counts[k] != 0], reverse=True)
        if not keys:
            return None
        node = head = PolyNode(counts[keys[0]], keys[0])
        for i in range(1, len(keys)):
            node.next = PolyNode(counts[keys[i]], keys[i])
            node = node.next
        return head

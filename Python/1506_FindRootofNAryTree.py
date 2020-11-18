"""
Given all the nodes of an N-ary tree as an array  Node[] tree where each node has a unique value.

Find and return the root of the N-ary tree.

 

Follow up:

Could you solve this problem in constant space complexity with a linear time algorithm?

 

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



For example, the above tree is serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].


Custom testing:
You should provide the serialization of the input tree.
The Driver code then extracts the nodes from the tree and shuffles them. You shouldn't care how the extracted nodes are shuffled.
The driver code will provide you with an array of the extracted nodes in random order and you need to find the root of the tree out of these nodes.

 

Example 1:



Input: tree = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Explanation: The input tree is shown above. The driver code first extracts the nodes so we now have an array of all tree nodes [Node(1),Node(3),Node(2),Node(4),Node(5),Node(6)], then the array is randomly shuffled, thus the actual input is [Node(5),Node(4),Node(3),Node(6),Node(2),Node(1)].
The root of the tree is Node(1) and the output is the serialization of the node you return.
Example 2:



Input: tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 

Constraints:

The total number of nodes is between [1, 5 * 10^4].
Each node has a unique value.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-root-of-n-ary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

from functools import lru_cache
class Solution:
    def findRoot(self, tree) -> 'Node':
        @lru_cache(None)
        def dfs(node):
            if not node:
                return 0
            return 1 + sum(dfs(n_node) for n_node in node.children)

        res, counts = None, 0
        for node in tree:
            tmp = dfs(node)
            if tmp > counts:
                res = node
                counts = tmp
        return res
# https://leetcode-cn.com/problems/find-root-of-n-ary-tree/solution/li-yong-jie-dian-quan-zhi-hu-bu-xiang-tong-de-xing/
# 对于非根节点，它会在 tree 列表中出现一次，并且在某个节点的 children 列表中出现一次，一共出现两次。

# 对于根节点，它只会在 tree 列表中出现一次。

# 因此我们遍历所有的节点以及它们的子节点，进行按位异或运算，由于一个数按位异或两次等于没有进行任何运算，因此最后运算的结果就是根节点的权值。

# 由于树中节点权值互不相同，我们再遍历一遍 tree 列表找出该节点即可。

# 作者：zerotrac2
# 链接：https://leetcode-cn.com/problems/find-root-of-n-ary-tree/solution/li-yong-jie-dian-quan-zhi-hu-bu-xiang-tong-de-xing/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def findRoot(self, tree) -> 'Node':
        xor = 0
        for node in tree:
            xor ^= node.val
            for child in node.children:
                xor ^= child.val

        for node in tree:
            if node.val == xor:
                return node
        return None


from collections import Counter, defaultdict, OrderedDict, deque
from bisect import bisect_left, bisect_right 
from functools import reduce, lru_cache 
from typing import List 
import itertools 
import math 
import heapq 
import string
true = True
false = False
MIN, MAX, MOD = -0x3f3f3f3f, 0x3f3f3f3f, 1000000007

# https://leetcode.com/problems/find-root-of-n-ary-tree/description/
# Medium
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        ans = 0
        for t in tree:
            ans ^= t.val
            for c in t.children:
                ans ^= c.val
        return next(filter(lambda t: t.val == ans, tree))



# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/find-root-of-n-ary-tree/solution/python-jian-dan-ji-he-ying-yong-by-hao-shou-bu-jua/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        impossible = set()
        all_node = set()
        for node in tree:
            for child in node.children:
                impossible.add(child)
            all_node.add(node)

        return list(all_node-impossible)[0]


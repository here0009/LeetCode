"""
Given the root of an N-ary tree of unique values, and two nodes of the tree p and q.

You should move the subtree of the node p to become a direct child of node q. If p is already a direct child of q, don't change anything. Node p must be the last child in the children list of node q.

Return the root of the tree after adjusting it.

 

There are 3 cases for nodes p and q:

Node q is in the sub-tree of node p.
Node p is in the sub-tree of node q.
Neither node p is in the sub-tree of node q nor node q is in the sub-tree of node p.
In cases 2 and 3, you just need to move p (with its sub-tree) to be a child of q, but in case 1 the tree may be disconnected, thus you need to reconnect the tree again. Please read the examples carefully before solving this problem.

 

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



For example, the above tree is serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

 

Example 1:


Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 4, q = 1
Output: [1,null,2,3,4,null,5,null,6,null,7,8]
Explanation: This example follows the second case as node p is in the sub-tree of node q. We move node p with its sub-tree to be a direct child of node q.
Notice that node 4 is the last child of node 1.
Example 2:


Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 7, q = 4
Output: [1,null,2,3,null,4,5,null,6,null,7,8]
Explanation: Node 7 is already a direct child of node 4. We don't change anything.
Example 3:


Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 3, q = 8
Output: [1,null,2,null,4,5,null,7,8,null,null,null,3,null,6]
Explanation: This example follows case 3 because node p is not in the sub-tree of node q and vice-versa. We can move node 3 with its sub-tree and make it as node 8's child.
Example 4:


Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 2, q = 7
Output: [1,null,7,3,null,2,null,6,null,4,5,null,null,8]
Explanation: Node q is in the sub-tree of node p, so this is case 1.
The first step, we move node p (with all of its sub-tree except for node q) and add it as a child to node q.
Then we will see that the tree is disconnected, you need to reconnect node q to replace node p as shown.
Example 5:


Input: root = [1,null,2,3,null,4,5,null,6,null,7,8], p = 1, q = 2
Output: [2,null,4,5,1,null,7,8,null,null,3,null,null,null,6]
Explanation: Node q is in the sub-tree of node p, so this is case 1.
The first step, we move node p (with all of its sub-tree except for node q) and add it as a child to node q.
As node p was the root of the tree, node q replaces it and becomes the root of the tree.
 

Constraints:

The total number of nodes is between [2, 1000].
Each node has a unique value.
p != null
q != null
p and q are two different nodes (i.e. p != q).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-sub-tree-of-n-ary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        def inSubtree(i, j):
            """
            return if j is in the subtree of i
            """
            if i == j:
                return True
            return any(inSubtree(k, j) for k in i.children)

        def removeNode(i, j):
            if not i:
                return None
            print(i.val, j.val)
            for k in range(len(i.children)):
                if i.children[k] == j:
                    i.children.pop(k)
                    return i
            for ni in i.children:
                tmp = removeNode(ni, j)
                if tmp is not None:
                    return tmp
            return None

        head = Node(0, [root])
        if p in q.children:
            return root
        print(inSubtree(p, q))
        if inSubtree(p, q): #q is in the subtree of p
            removeNode(p, q)
        p_parent = removeNode(head, p)
        q.children.append(p)
        p_parent.children.append(q)
        return head.children[0]
# 作者：yuan-zhi-b
# 链接：https://leetcode-cn.com/problems/move-sub-tree-of-n-ary-tree/solution/python3-qi-shi-zhi-you-2chong-qing-kuang-by-yuan-z/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    dummy=Node()
    dummy.children.append(root)
    pParent,qParent,is_p_over_q=None,None,False
    def dfs(node,parent,is_under_p):
        nonlocal pParent,qParent,is_p_over_q
        if node==p:
            pParent,is_under_p=parent,True
        if node==q:
            if is_under_p:
                is_p_over_q=True                
            qParent=parent
        for child in node.children:
            dfs(child,node,is_under_p)
    dfs(root,dummy,False)
    if pParent==q:
        return root
    if is_p_over_q:
        qParent.children.remove(q)
        idx=pParent.children.index(p)
        pParent.children[idx]=q
        q.children.append(p)
    else:
        pParent.children.remove(p)
        q.children.append(p)
    return dummy.children[0]



class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
        """
        Thoughts: 
        1. find the parent of p, parent of q
        2. add p to the children of q
        3. add q to the parent of p
        """
        def dfs(node):
            if not node:
                return
            for i,v in enumerate(node.children):
                if v is p:
                    self.p_parent = node
                    self.p_index = i
                if v is q:
                    self.q_parent = node
                    self.q_index = i
                dfs(v)

        def inSubtree(i, j):
            """
            return if j is in the subtree of i
            """
            if i == j:
                return True
            return any(inSubtree(k, j) for k in i.children)

        if p in q.children:
            return root

        dummy = Node(0, [root])
        self.p_parent, self.p_index = None, None
        self.q_parent, self.q_index = None, None
        dfs(dummy)
        if inSubtree(p, q):
            self.q_parent.children.pop(self.q_index)
            self.p_parent.children.pop(self.p_index)
            self.p_parent.children.insert(self.p_index, q)
        else:
            self.p_parent.children.pop(self.p_index)

        q.children.append(p)
        return dummy.children[0]


# test case
# [1,null,2,3,null,4,5,null,6,null,7,8]
# 4
# 1

# [1,null,2,3,null,4,5,null,6,null,7,8]
# 7
# 4

# [1,null,2,3,null,4,5,null,6,null,7,8]
# 3
# 8

# [1,null,2,3,null,4,5,null,6,null,7,8]
# 2
# 7

# [1,null,2,3,null,4,5,null,6,null,7,8]
# 1
# 2

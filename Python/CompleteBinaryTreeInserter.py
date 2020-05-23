"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
 

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]
 

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter_1:

    def __init__(self, root: TreeNode):
        self.root = root
        

    def insert(self, v: int) -> int:
        insert_node = TreeNode(v)
        bfs = [self.root]
        bfs2 = []
        while len(bfs) > 0:
            for node in bfs:
                if not node.left:
                    node.left = insert_node
                    return node.val
                elif not node.right:
                    node.right = insert_node
                    return node.val
                else:
                    bfs2.extend([node.left,node.right])
            bfs = bfs2

    def get_root(self) -> TreeNode:
        return self.root


from collections import deque
class CBTInserter:
    """
    use deque, the insertion will be more faster
    dq is the list of bfs traverse of the tree
    dq contains all node that is incomplete
    """
    def __init__(self, root: TreeNode):
        self.root = root
        self.dq = deque()
        q = deque([self.root]) #bfs check all the node
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.dq.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        
    def insert(self, v: int) -> int:
        insert_node = TreeNode(v)
        self.dq.append(insert_node)
        node = self.dq[0]
        if not node.left:
            node.left = insert_node
        else:
            node.right = insert_node
            self.dq.popleft()
        return node.val
        

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
obj = CBTInserter(root)
param_1 = obj.insert(v)
param_2 = obj.get_root()
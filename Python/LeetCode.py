class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def constructListNode(input_list):
    """
    construct listnode from list
    e.g: l1 = s.constructListNode([7,2,4,3])
    """
    root = ListNode(0)
    curr = root
    for i in range(len(input_list)):
        curr.next = ListNode(input_list[i])
        curr = curr.next
    return root.next

def printListNode(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)
    
import pysnooper
class Solution:
    @pysnooper.snoop('./pysnooper.log')
    def numSubarrayProductLessThanK(self, nums, k):
        pass

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Tree_Builds_BFS(node_val_list):
    if len(node_val_list) == 0:
        return None
    node_list = []
    for index, val in enumerate(node_val_list):
        if val is not None:
            node = TreeNode(val)
            # print(val)
        else:
            node = None
        if index == 0:
            root = node
            node_list.append(root)
        else:

            if index%2:
                tmp = node_list[index//2]
                tmp.left = node
            else:
                tmp = node_list[index//2-1]
                tmp.right = node
            node_list.append(node)
    return root

def treeLevel(root):
    """
    return the depth of the tree
    """

    if not root:
        return 0
    else:
        return 1+max(treeLevel(root.left),treeLevel(root.right))

from collections import deque
def printBinaryTree(root):
    """
    print the binary tree, not very elegant now
    """
    level = treeLevel(root)
    q = deque([root])
    while level > 0:
        new_q = deque()
        while q:
            tmp = q.popleft()
            if tmp:
                new_q.append(tmp.left)
                new_q.append(tmp.right)
                print(level*' ', tmp.val, end='')
        print('\n')
        q = new_q
        level -= 1
    return


def construcTree(voyage):
    """
    contruct a tree from a list named voyage, e.g: [1,2,3,None,None,4,5]
      1
     / \
    2   3
        /\
       4  5
    """
    def treeNode(val):
        if val is None:
            return None
        else:
            return TreeNode(val)

    v_root = TreeNode(voyage[0])
    bfs = deque([v_root])
    index = 0
    len_v = len(voyage)
    while bfs and index < len_v:
        node = bfs.popleft()
        if index+1 < len_v:
            node.left = treeNode(voyage[index+1])
        if index+2 < len_v:
            node.right = treeNode(voyage[index+2])
        if node.left:
            bfs.append(node.left)
        if node.right:
            bfs.append(node.right)
        index += 2
    return v_root
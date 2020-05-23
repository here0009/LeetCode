"""
Suppose that all the keys in a binary tree are distinct positive integers. Given the postorder and inorder traversal sequences, you are supposed to output the level order traversal sequence of the corresponding binary tree.

Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (≤30), the total number of nodes in the binary tree. The second line gives the postorder sequence and the third line gives the inorder sequence. All the numbers in a line are separated by a space.

Output Specification:
For each test case, print in one line the level order traversal sequence of the corresponding binary tree. All the numbers in a line must be separated by exactly one space, and there must be no extra space at the end of the line.

Sample Input:
7
2 3 1 5 7 6 4
1 2 3 4 5 6 7
Sample Output:
4 1 6 3 5 7 2
"""
import sys
sys.stdin = open('input.txt')
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construcTree(postorder, inorder):
    """
    construct a tree from postorder and inorder traverse only if the inputs is the postorder and inorder traverse of a tree
    """
    if len(postorder) == 0:
        return None
    root_num = postorder[-1]
    root = Node(root_num)
    root_index = inorder.index(root_num) #root index is also the length of left tree
    root.left = construcTree(postorder[:root_index] ,inorder[:root_index])
    root.right = construcTree(postorder[root_index:-1] ,inorder[root_index+1:])
    return root

def BFS(root):
    """
    breadth first traverse of root
    """ 
    if not root:
        return []
    
    stack = [root]
    res = [root.val]
    while stack:
        stack2 = []
        for node in stack:
            if node.left:
                stack2.append(node.left)
                res.append(node.left.val)
            if node.right:
                stack2.append(node.right)
                res.append(node.right.val)
        stack = stack2
    return res

N = int(input())
postorder = [int(i) for i in input().split()]
inorder = [int(i) for i in input().split()]
root = construcTree(postorder, inorder)
res = BFS(root)
res_str = ' '.join([str(i) for i in res])
print(res_str)
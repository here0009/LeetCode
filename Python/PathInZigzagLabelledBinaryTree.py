"""
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
"""
class Solution:
    def pathInZigZagTree(self, label: int):
        index = [1]
        res = []
        while index[-1] < label:
            index.append(index[-1]*2+1) #use index to record the last index of each level
        # print(index)
        index.pop()  
        res.append(label) #pop the last index and append the original label to res
        while index:
            label  = label//2
            last = index.pop()
            first = (last+1)//2 
            label = first + last - label #the zigzag lable is the mirror of the original lable in each level
            res.append(label)
        return res[::-1]

s = Solution()
label = 14
print(s.pathInZigZagTree(label))
label = 26
print(s.pathInZigZagTree(label))
label = 1
print(s.pathInZigZagTree(label))

"""
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

Example 1:

Input: [[1,1],2,[1,1]]
Output: 8 
Explanation: Four 1's at depth 1, one 2 at depth 2.
Example 2:

Input: [1,[4,[6]]]
Output: 17 
Explanation: One 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/nested-list-weight-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def depthSumInverse(self, nestedList) -> int:
        def depth(nestedList):
            if nestedList.isInteger():
                return 1
            lst = nestedList.getList()
            d = 1
            for elem in lst:
                d = max(d, depth(elem)+1)
            return d

        def dfs(nestedList, d):
            if nestedList.isInteger():
                return d*nestedList.getInteger()
            res = 0
            lst = nestedList.getList()
            for elem in lst:
                res += dfs(elem, d-1)
            return res

        root = NestedInteger()
        for elem in nestedList:
            root.add(elem)
        d = depth(root)
        return dfs(root, d)


# 作者：amchor
# 链接：https://leetcode-cn.com/problems/nested-list-weight-sum-ii/solution/zi-dian-fa-by-amchor/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from collections import defaultdict
class Solution:
    def depthSumInverse(self, nestedList) -> int:
        def dfs(nestedList, level):
            self.max_level = max(self.max_level, level)
            for elem in nestedList:
                if elem.isInteger():
                    depth_dict[level] += elem.getInteger()
                else:
                    dfs(elem.getList(), level + 1)

        self.max_level = 0
        depth_dict = defaultdict(int)
        dfs(nestedList, 1)
        self.max_level += 1
        res = 0
        for k, v in depth_dict.items():
            res += (self.max_level - k) * v
        return res




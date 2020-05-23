"""
It is a Bipartite Graph problem, can be solved with coloring.
The strategy is define a source point, and color it with red.
and the point link to the source point will be colored blue.
go on with this process until every dots have been colored, if you encounter a dot that will be colored both red and blue, return false, otherwise, return true.
"""
class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        color_dict = dict()
        if N == 1: # N >= 1
            return False
        if len(dislikes) == 0: # dislikes >= 0
            return True
        for i in N:
            color_dict[i] = -1 # use number instead of string for coloring, -1 for black, 0 for red and 1 for blue.
        i,j = dislikes[0]
        color_dict[i] = 0
        color_dict[j] = 1
        for dislike in dislikes[1:]:


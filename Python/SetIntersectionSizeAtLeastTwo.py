"""
An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.

Example 1:
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.
Note:

intervals will have length in range [1, 3000].
intervals[i] will have length 2, representing some integer interval.
intervals[i][j] will be an integer in [0, 10^8].
"""


class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        """
        wrong answer, the answer is set it did not have to be continuous
        """
        intervals = sorted(intervals, key = lambda x : x[1])
        # print(intervals)
        start, end = intervals[0][-1]-1, intervals[0][-1]
        for p, q in intervals[1:]:
            end = max(end, p+1)
            # print(p,q,start, end)
        return end-start+1


class Solution:
    def intersectionSizeTwo(self, intervals) -> int:
        # Sort intervals by ending points
        # Greedily select two largest numbers in interval as needed
        # KEY: We only need to look at the two largest numbers added thus far (last added) to our picks list.
        intervals = sorted(intervals, key=lambda x: x[1])
        a,b = intervals[0][-1]-1, intervals[0][-1]  # the right most elment we want to use
        res = 2
        for p,q in intervals[1:]:
            if p > b:
                a,b = q-1, q
                res += 2
            elif p > a:
                a,b = b, q
                res += 1
        return res


S = Solution()
intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
print(S.intersectionSizeTwo(intervals))
intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
print(S.intersectionSizeTwo(intervals))
intervals = [[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]
print(S.intersectionSizeTwo(intervals))
# Output
# 4
# Expected
# 5
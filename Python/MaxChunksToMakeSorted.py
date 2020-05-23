"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].
"""
class Solution:
    def maxChunksToSorted(self, arr) -> int:
        res = 0
        expected = set()
        max_v = None
        for i,v in enumerate(arr):
            if not expected:
                expected = set(range(i,v+1))
                max_v = v
            elif v > max_v:
                expected |= set(range(max_v+1,v+1))
                max_v = v
            # print(expected)
            expected -= {v}
            if len(expected) == 0:
                res += 1
        return res

class Solution:
    def maxChunksToSorted(self, arr) -> int:
        """
        Thoughts: store the current max value, if index == curr_max, then the values that smaller than curr_max must have benn visted before, so the chunk can split from arr
        """
        res = 0
        curr_max = 0
        for i,v in enumerate(arr):
            curr_max = max(v,curr_max)
            if curr_max == i:
                res += 1
        return res

s = Solution()
arr = [4,3,2,1,0]
print(s.maxChunksToSorted(arr))

arr = [1,0,2,3,4]
print(s.maxChunksToSorted(arr))

arr = [1,2,0,3]
print(s.maxChunksToSorted(arr))

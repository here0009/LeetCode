"""
You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

 

Example 1:

Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
Example 2:

Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]
 

Constraints:

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109
"""
# class Trie:

#     def __init__(self, children):
#         self.children 


from typing import List
from collections import defaultdict
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Thoughts:
        sort nums
        sort quries based on m
        insert num to trie if num <= m
        search for num that xor diff with x from high digit to low digit.
        because num < 10**9, then 2**31 is enough
        """
        def insert(node, num):
            # print(node, num)

            for i in range(31, -1, -1):
                d = (num >> i) & 1
                if d not in node:
                    node[d] = dict()
                node = node[d]
            node['$'] = num

        def search(node, num):
            for i in range(31, -1, -1):
                d = (num >> i) & 1
                if 1 - d in node:
                    node = node[1 - d]
                else:
                    node = node[d]
            return node['$']


        root = dict()
        nums.sort()
        len_nums = len(nums)
        queries = sorted((m, i, x) for i, (x, m) in enumerate(queries))
        index = 0
        res = [-1] * len(queries)
        for m, i, x in queries:
            while index < len_nums and nums[index] <= m:
                insert(root, nums[index])
                index += 1
            if root:
                res[i] = search(root, x) ^ x
        return res


from collections import defaultdict
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Thoughts:
        sort nums
        sort quries based on m
        insert num to trie if num <= m
        search for num that xor diff with x from high digit to low digit.
        because num < 10**9, then 2**31 is enough
        """
        def insert(node, num):
            # print(node, num)

            for i in range(31, -1, -1):
                d = (num >> i) & 1
                if d not in node:
                    node[d] = dict()
                node = node[d]
            node['$'] = num

        def search(node, num):
            for i in range(31, -1, -1):
                d = (num >> i) & 1
                if 1 - d in node:
                    node = node[1 - d]
                else:
                    node = node[d]
            return node['$']


        root = dict()
        nums.sort()
        len_nums = len(nums)
        queries = sorted((m, i, x) for i, (x, m) in enumerate(queries))
        index = 0
        res = [-1] * len(queries)
        for m, i, x in queries:
            while index < len_nums and nums[index] <= m:
                insert(root, nums[index])
                index += 1
            if root:
                res[i] = search(root, x) ^ x
        return res


class Trie:
    def __init__(self):
        self.root = {}

    def __bool__(self):
        return len(self.root) > 0

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            d = (num >> i) & 1
            if d not in node:
                node[d] = dict()
            node = node[d]
        node['$'] = num

    def search(self, num):
        node = self.root
        for i in range(31, -1, -1):
            d = (num >> i) & 1
            if 1 - d in node:
                node = node[1 - d]
            else:
                node = node[d]
        return node['$']

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Thoughts:
        sort nums
        sort quries based on m
        insert num to trie if num <= m
        search for num that xor diff with x from high digit to low digit.
        because num < 10**9, then 2**31 is enough
        """
        root = Trie()
        nums.sort()
        len_nums = len(nums)
        queries = sorted((m, i, x) for i, (x, m) in enumerate(queries))
        index = 0
        res = [-1] * len(queries)
        for m, i, x in queries:
            while index < len_nums and nums[index] <= m:
                root.insert(nums[index])
                index += 1
            if root:
                res[i] = root.search(x) ^ x
        return res

S = Solution()
nums = [0,1,2,3,4]
queries = [[3,1],[1,3],[5,6]]
print(S.maximizeXor(nums, queries))
nums = [5,2,4,6,6,3]
queries = [[12,4],[8,1],[6,3]]
print(S.maximizeXor(nums, queries))

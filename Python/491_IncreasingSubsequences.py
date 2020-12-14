"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""


from collections import Counter
class Solution:
    def findSubsequences(self, nums):
        """
        wrong answer, you can not sort nums
        """
        def dfs(lst, i, k):
            """
            i is the index of keys, r is the remaning character
            """
            # print(lst, i, k)
            if k == 0:
                self.res.append(lst)
                return
            if i == len_k:
                return
            v = keys[i]
            min_c = min(counts[v], k)  # the max letter we can take keys[i]
            for j in range(min_c + 1):
                lst2 = lst + [v] * j
                dfs(lst2, i + 1, k - j)

        length = len(nums)
        counts = Counter(nums)
        keys = sorted(counts.keys())
        # print(counts, keys)
        len_k = len(keys)
        self.res = []
        for k in range(2, length+1):
            dfs([], 0, k)
        return self.res



from collections import Counter
class Solution:
    def findSubsequences(self, nums):
        def dfs(lst, i, k):
            """
            i is the index of keys, r is the remaning character
            """
            # print(lst, i, k)
            if k == 0:
                self.res.append(lst)
                return
            if i == len_k:
                return
            v = keys[i]
            min_c = min(counts[v], k)  # the max letter we can take keys[i]
            for j in range(min_c + 1):
                lst2 = lst + [v] * j
                dfs(lst2, i + 1, k - j)

        length = len(nums)
        counts = Counter(nums)
        keys = sorted(counts.keys())
        # print(counts, keys)
        len_k = len(keys)
        self.res = []
        for k in range(2, length+1):
            dfs([], 0, k)
        return self.res


from collections import defaultdict
class Solution:
    def findSubsequences(self, nums):
        """
        use a set to store the results (tuples) to avoid duplications
        for a num in nums, if a element before num is also <= num, construct a new subsequence
        """
        dp = defaultdict(set)
        res = set()
        len_nums = len(nums)
        for i in range(len_nums):
            dp[i].add(tuple([nums[i]]))
        for i in range(1, len_nums):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for t in dp[j]:
                        t2 = t + tuple([nums[i]])
                        if t2 not in res:
                            res.add(t2)
                            dp[i].add(t2)
        return [list(t) for t in res]


S = Solution()
nums = [4, 6, 7, 7]
print(S.findSubsequences(nums), len(S.findSubsequences(nums)))
print(len([[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]))
nums = [4,3,2,1]
print(S.findSubsequences(nums))
# Output
# [[3,4],[2,4],[2,3],[1,4],[1,3],[1,2],[2,3,4],[1,3,4],[1,2,4],[1,2,3],[1,2,3,4]]
# Expected
# []
nums = [3, 5, 7, 6, 4, 4, 8, 9]
print(S.findSubsequences(nums))
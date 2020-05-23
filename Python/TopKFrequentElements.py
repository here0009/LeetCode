"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from collections import Counter
class Solution_1:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_counter = Counter(nums)
        num_fre_list = [(value,key) for key,value in num_counter.items()]
        num_fre_list = sorted(num_fre_list, reverse = True)
        res = [item[1] for item in num_fre_list[:k]]
        return res

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_counter = Counter(nums)
        return [key for key, _ in num_counter.most_common(k)]


from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter_nums = Counter(nums)
        keys = sorted(counter_nums.keys(), key = lambda x:(-counter_nums[x],x))
        # print(keys)
        return keys[:k]

s = Solution()
nums = [1,1,1,2,2,3]
k = 2 
print(s.topKFrequent(nums, k))

nums = [1]
k = 1 
print(s.topKFrequent(nums, k))

# c = Counter()
# print(dir(c))
# print(help(Counter))
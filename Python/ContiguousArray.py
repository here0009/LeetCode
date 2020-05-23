"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
class Solution:
    def findMaxLength(self, nums) -> int:
        """
        TLE
        """
        seen = set()
        seen.add((0,0))
        res = 0
        counts = [0,0]
        for n in nums:
            counts[n] += 1
            for length in range(min(counts),res,-1):
                if (counts[0]-length, counts[1]-length) in seen:
                    res = length
                    break
            seen.add(tuple(counts))
            # print(seen)
        return res*2

class Solution:
    def findMaxLength(self, nums) -> int:
        """
        Thoughts: use a dict to record the min index of ones-zeros, so update the max length along nums
        """
        gaps_dict = {0:-1} #store min index of ones-zeros
        counts = [0,0]
        res = 0
        for i,v in enumerate(nums):
            counts[v] += 1
            gap = counts[1] - counts[0]
            if gap in gaps_dict:
                res = max(res, i - gaps_dict[gap])
            else:
                gaps_dict[gap] = i
        return res

s = Solution()
nums = [0,1]
print(s.findMaxLength(nums))

nums = [0,1,0]
print(s.findMaxLength(nums))

nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
print(s.findMaxLength(nums))
"""
Output
54
Expected
68
"""
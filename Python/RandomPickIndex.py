"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import random
from collections import defaultdict
class Solution:

    def __init__(self, nums):
        self.dict = defaultdict(list)
        for i,v in enumerate(nums):
            self.dict[v].append(i)
        # print(self.dict)    
    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
nums = [1,2,3,3,3]
s = Solution(nums)
for i in range(10):
    print(s.pick(1))
"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
import random
class Solution:

    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        res = []
        nums_copy = self.nums[:]
        n = self.len-1
        while n >= 0:
            index = random.randint(0,n)
            res.append(nums_copy.pop(index))
            n -= 1
        return res

        


# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())


nums = [1,2,3,7,8,0,123]
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())

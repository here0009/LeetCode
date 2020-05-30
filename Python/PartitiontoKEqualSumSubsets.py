"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""



class Solution:
    """
    Thoughts: fill bucket
    """
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        nums = sorted(nums, reverse=True)
        # print('nums:', nums)
        buckets = [0]*k
        target = sum(nums)/k
        length = len(nums)

        def dfs(index):
            if index == length:
                return len(set(buckets)) == 1
            for j in range(k):
                buckets[j] += nums[index]
                if buckets[j] <= target and dfs(index+1):
                    return True
                buckets[j] -= nums[index]
                if buckets[j] == 0:
                    break
                # This sentence is pure magic. Decrease the time from 2300ms to 30 ms!
                # Without this sentence, we are actually making each bucket unique.
                # However, it doesn't make sense because all buckets have the same size and they are the same.
                # If a single number couldn't fit into one bucket, it is a waste of time to put it into the other bucket.
                # adamzjk also mentioned the reason and it helps.
            return False
        return dfs(0)


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        def dfs(k,index,currSum):
            if currSum == target:
                if k == 1:
                    return True
                else:
                    return dfs(k - 1, 0, 0)
            for i in range(index, length):
                if not visit[i] and nums[i] + currSum <= target:
                    visit[i] = 1
                    if dfs(k, i+1, currSum+nums[i]):
                        return True
                    visit[i] = 0
            return False

        length = len(nums)
        visit = [0]*length
        if sum(nums) % k != 0 or k > sum(nums):
            return False
        target = sum(nums) //k
        return dfs(k,0,0)


S = Solution() 
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(S.canPartitionKSubsets(nums, k))


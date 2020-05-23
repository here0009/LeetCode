"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""


class Solution_1:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        length = len(nums)
        val_index = sorted([(v,i) for i,v in enumerate(nums)]) #sort by value

        for i in range(length):
            s_v,s_i = val_index[i]
            for j in range(i+1, length):
                e_v,e_i = val_index[j]
                if e_v - s_v > t:
                    break
                else:
                    if abs(s_i - e_i) <= k:
                        return True
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        """
        TLE
        """
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1,i+k+1):
                if j < length:
                    if abs(nums[i]-nums[j]) <= t:
                        return True
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        """
        use a bucket to store 
        """
        if t < 0 or k < 0:
            return False
        bucket = dict()
        distance = t+1
        # print('-------------')
        for i,v in enumerate(nums):
            # print('bucket',v, bucket)
            bucket_id = v//distance
            for b_id in [bucket_id-1, bucket_id, bucket_id+1]:
                if (b_id in bucket) and (abs(bucket[b_id] - v) <= t):
                    return True
            bucket[bucket_id] = v
            if i-k >= 0:
                del bucket[nums[i-k]//distance] #the diff index between i+1 to i-k is k+1, so pop i-k
        return False


S = Solution()
nums = [1,2,3,1]
k = 3
t = 0
print(S.containsNearbyAlmostDuplicate(nums, k, t))
nums = [1,0,1,1]
k = 1
t = 2
print(S.containsNearbyAlmostDuplicate(nums, k, t))
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(S.containsNearbyAlmostDuplicate(nums, k, t))

nums = [1,3,6,2]
k = 1
t = 2
print(S.containsNearbyAlmostDuplicate(nums, k, t))


nums = [-1,-1]
k = 1
t = -1
print(S.containsNearbyAlmostDuplicate(nums, k, t))

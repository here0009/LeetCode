"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
class Solution_1:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Thoughts:
        from the start, get the product of nums, break when it is not less than k. Record the break point e_i.
        from the end, get the product of nums, break when it is not less than k. Record the break point s_i.
        the subarrays are nums[:e_i], nums[s_i, e_i], nums[s_i:]
        """
        product_s, product_e = 1, 1
        e_i, s_i = 0, len(nums)-1
        while e_i < len(nums):
            product_s *= nums[e_i]
            if product_s >= k:
                break
            e_i+=1
            
import pysnooper
class Solution:
    # @pysnooper.snoop('./pysnooper.log')
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Thoughts:
        multiply from the beginning, coninue multiply until not smaller than k, then divide the beginning, start a new multipy
        the subarry number of k elements is k+k*(k-1)/2 = k(k+1)/2
        """
        product = 1
        res = 0
        index, start, end = 0, 0, 0
        while index < len(nums):
            if nums[index] >= k:
                res += (end-start+1)*(end-start)//2
                start = index + 1
                end = index + 1
                product = 1
                
            else:
                product = product * nums[index]
                if product < k:
                    end += 1
                else:
                    res += (end-start+1)*(end-start)//2
                    while product >=k:
                        product = product // nums[start]
                        start += 1
                    res -= (end-start+1)*(end-start)//2 #minus the overlap
                    end += 1
            index += 1
        res += (end-start+1)*(end-start)//2
        return res

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Thoughts:
        using sliding window, every time we add a new element to the sliding window, the number of subarrays increase  end-start+1, end-start for subarray that start with previous elments, end with end. 1 for end itself
        """
        start, end, product, res = 0, 0, 1, 0
        if k <= 1 : return 0
        for end in range(len(nums)):
            product = product * nums[end]
            while product >= k:
                product = product // nums[start]
                start += 1
            res += end-start + 1
        return res


s = Solution()
nums = [10, 5, 2, 6]
k = 100
print(s.numSubarrayProductLessThanK(nums,k))


                         

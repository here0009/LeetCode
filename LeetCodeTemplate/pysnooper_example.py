import pysnooper
class Solution:
    @pysnooper.snoop('./pysnooper.log')
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
                    end = index
            index += 1
        res += (end-start+1)*(end-start)//2
        return res
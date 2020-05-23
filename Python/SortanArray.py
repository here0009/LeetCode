"""
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Note:

1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""
import pysnooper
class Solution:
    @pysnooper.snoop('./pysnooper.log')
    def sortArray(self, nums):
        """
        merge sort
        """
        def merge(p,q):
            """
            merge two already sorted list p and q
            """
            res,i,j = [],0,0
            while i < len(p) and j < len(q):
                if p[i] < q[j]:
                    res.append(p[i])
                    i+= 1
                else:
                    res.append(q[j])
                    j+=1
            while i < len(p):
                res.append(p[i])
                i+= 1
            while j < len(q):
                res.append(q[j])
                j+=1
            return res

        def mergeSort(k):
            print(k)
            if len(k) == 1:
                return k
            if len(k) == 2:
                if k[1] < k[0]:
                    return [k[1],k[0]]
                return k
            middle = len(k)//2
            p = mergeSort(nums[:middle])
            q = mergeSort(nums[middle:])
            res = merge(p,q)
            return res

        return mergeSort(nums)


class Solution:
    def sortArray(self, nums):
        if len(nums) > 1:
            middle = len(nums)//2
            p = nums[:middle]
            q = nums[middle:]
            self.sortArray(p)
            self.sortArray(q)
            k,i,j = 0,0,0
            while i < len(p) and j < len(q):
                if p[i] < q[j]:
                    nums[k] = p[i]
                    i+= 1
                else:
                    nums[k] = q[j]
                    j+=1
                k+=1
            while i < len(p):
                nums[k] = p[i]
                i+= 1
                k+=1
            while j < len(q):
                nums[k] = q[j]
                j+=1
                k+=1
        return nums
import random
class Solution_2:
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        k = random.choice(nums)
        lt = [v for v in nums if v < k]
        eq = [v for v in nums if v == k]
        gt = [v for v in nums if v > k]
        return self.sortArray(lt) + eq + self.sortArray(gt)
             
s = Solution_2()
nums = [5,2,3,1]
print(s.sortArray(nums))

nums = [5,1,1,2,0,0]
print(s.sortArray(nums))
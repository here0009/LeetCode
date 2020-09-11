"""
Given two arrays of integers nums1 and nums2, return the number of triplets formed (type 1 and type 2) under the following rules:

Type 1: Triplet (i, j, k) if nums1[i]2 == nums2[j] * nums2[k] where 0 <= i < nums1.length and 0 <= j < k < nums2.length.
Type 2: Triplet (i, j, k) if nums2[i]2 == nums1[j] * nums1[k] where 0 <= i < nums2.length and 0 <= j < k < nums1.length.
 

Example 1:

Input: nums1 = [7,4], nums2 = [5,2,8,9]
Output: 1
Explanation: Type 1: (1,1,2), nums1[1]^2 = nums2[1] * nums2[2]. (4^2 = 2 * 8). 
Example 2:

Input: nums1 = [1,1], nums2 = [1,1,1]
Output: 9
Explanation: All Triplets are valid, because 1^2 = 1 * 1.
Type 1: (0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2).  nums1[i]^2 = nums2[j] * nums2[k].
Type 2: (0,0,1), (1,0,1), (2,0,1). nums2[i]^2 = nums1[j] * nums1[k].
Example 3:

Input: nums1 = [7,7,8,3], nums2 = [1,2,9,7]
Output: 2
Explanation: There are 2 valid triplets.
Type 1: (3,0,2).  nums1[3]^2 = nums2[0] * nums2[2].
Type 2: (3,0,1).  nums2[3]^2 = nums1[0] * nums1[1].
Example 4:

Input: nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
Output: 0
Explanation: There are no valid triplets.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5
"""


from collections import Counter
from itertools import combinations
class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        c_nums1 = Counter(nums1)
        c_nums2 = Counter(nums2)
        res = 0
        self_product1 = Counter()
        cross_product1 = Counter()
        self_product2 = Counter()
        cross_product2 = Counter()

        for k, v in c_nums1.items():
            self_product1[k**2] += v*(v-1)//2
        for k, v in c_nums2.items():
            self_product2[k**2] += v*(v-1)//2

        for comb in combinations(c_nums1.keys(), 2):
            p, v = comb
            cross_product1[p*v] += c_nums1[p]*c_nums1[v]
        for comb in combinations(c_nums2.keys(), 2):
            p, v = comb
            cross_product2[p*v] += c_nums2[p]*c_nums2[v]

        for k,v in c_nums1.items():
            target = k**2
            if target in cross_product2:
                res += v*cross_product2[target]
            if target in self_product2:
                res += v*self_product2[target]

        for k,v in c_nums2.items():
            target = k**2
            if target in cross_product1:
                res += v*cross_product1[target]
            if target in self_product1:
                res += v*self_product1[target]
        return res
        # print(self_product1)
        # print(cross_product1)


from collections import Counter
class Solution:
    def numTriplets(self, nums1, nums2) -> int:
        d1 = Counter()
        d2 = Counter()
        for i in nums1:
            d1[i * i] += 1
        for i in nums2:
            d2[i * i] += 1
        res = 0
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                res += d2[nums1[i] * nums1[j]]
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                res += d1[nums2[i] * nums2[j]]
        return res
        

S = Solution()
nums1 = [7,4]
nums2 = [5,2,8,9]
print(S.numTriplets(nums1, nums2))
nums1 = [1,1]
nums2 = [1,1,1]
print(S.numTriplets(nums1, nums2))
nums1 = [7,7,8,3]
nums2 = [1,2,9,7]
print(S.numTriplets(nums1, nums2))
nums1 = [4,7,9,11,23]
nums2 = [3,5,1024,12,18]
print(S.numTriplets(nums1, nums2))
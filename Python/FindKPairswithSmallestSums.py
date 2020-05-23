"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        """
        wrong ans
        """
        res = []
        l1,l2,len_res = len(nums1),len(nums2),0
        i1,i2 = 0,0
        while i1 < l1 and i2 < l2 and len_res < k:
            print(i1,i2)
            res.append([nums1[i1],nums2[i2]])
            len_res += 1
            if i2+1 >= l2:
                i1 += 1
            elif i1+1 >= l1:
                i2 += 1
            else:
                if nums1[i1+1] <= nums2[i2+1]:
                    i1 += 1
                else:
                    i2 += 1
        return res

class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        res = sorted([[i,j] for i in nums1 for j in nums2], key = lambda x: x[0]+x[1])
        return res[:k]

import heapq
class Solution:
    """
    try to use heap, no need to sort all the sums
    """
    def kSmallestPairs(self, nums1, nums2, k: int):
        res = heapq.nsmallest(k, ([u,v] for u in nums1 for v in nums2), key = sum)
        return res
            

"""
The previous solution right away considered (the first pair of) all matrix rows (see visualization above). This one doesn't. It starts off only with the very first pair at the top-left corner of the matrix, and expands from there as needed. Whenever a pair is chosen into the output result, the next pair in the row gets added to the priority queue of current options. Also, if the chosen pair is the first one in its row, then the first pair in the next row is added to the queue.

Here's a visualization of a possible state:

# # # # # ? . .
# # # ? . . . .
# ? . . . . . .   "#" means pair already in the output
# ? . . . . . .   "?" means pair currently in the queue
# ? . . . . . .
? . . . . . . .
. . . . . . . .

steps for a 3*3 matrix
? * *
* * *
* * *

# ? *
? * *
* * *

# # ?
# ? *
? * *

# # #
# # ?
# ? *

# # #
# # #
# # ?

# # #
# # #
# # #
"""

import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):
        def push(i,j):
            if i < l1 and j < l2:
                heapq.heappush(queue, (nums1[i]+nums2[j], i,j))

        l1,l2 = len(nums1),len(nums2)
        res = []
        queue = []    
        push(0,0)
        while queue and len(res) < k:
            _,i,j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            push(i,j+1) #push the next candidate
            if j == 0:
                push(i+1,0)

        return res
    


S = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(S.kSmallestPairs(nums1,nums2, k))
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(S.kSmallestPairs(nums1,nums2, k))
nums1 = [1,2]
nums2 = [3]
k = 3
print(S.kSmallestPairs(nums1,nums2, k))

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print(S.kSmallestPairs(nums1,nums2, k))
# Output
# [[1,1],[1,1],[2,1],[2,2],[2,3]]
# Expected
# [[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]
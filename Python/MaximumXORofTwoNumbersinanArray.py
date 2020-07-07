"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2**31.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
class Solution:
    def findMaximumXOR(self, nums) -> int:
        len_n = len(nums)
        for i in range(len_n-1):
            for j in range(i+1, len_n):
                p = nums[i]
                q = nums[j]
                print(p,q,p^q)



class Solution:
    def findMaximumXOR(self, nums) -> int:
        """
        TLE
        """
        length = len(nums)
        res = 0
        for i in range(length - 1):
            for j in range(i+1, length):
                res = max(res, nums[i] ^ nums[j])
        return res

class Solution:
    def findMaximumXOR(self, nums) -> int:
        length = len(nums)
        res = 0
        for i in range(length - 1):
            for j in range(i+1, length):
                res = max(res, nums[i] ^ nums[j])
        return res


class TriNode():
    zero = None
    one = None
    val = None

class Solution:
    def findMaximumXOR(self, nums) -> int:
        bitRange = range(31, -1, -1)
        root = TriNode()
        for num in nums:
            curr = root
            for i in bitRange:
                v = num & (1 << i)
                if v == 0:
                    if not curr.zero:
                        curr.zero = TriNode()
                    curr = curr.zero
                else:
                    if not curr.one:
                        curr.one = TriNode()
                    curr = curr.one
            curr.val = num

        res = 0
        for num in nums:
            curr = root
            for i in bitRange:
                v = num & (1 << i)
                if v == 0:
                    if curr.one:
                        curr = curr.one
                    else:
                        curr = curr.zero
                else:
                    if curr.zero:
                        curr = curr.zero
                    else:
                        curr = curr.one
            # print(num, curr.val, res, num ^ curr.val)
            res = max(res, num ^ curr.val)
        return res



# class TrieNode():
#     zero = None
#     one = None
#     value = None

# class Solution:
#     def findMaximumXOR(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         root = TrieNode()
#         bit_range = range(31, -1, -1)       # [31, 30, .... 0]. We'll use this to iterate over num bit by bit.
#         for num in nums:
#             # always start at the top of the tree
#             curr = root
#             for i in bit_range:
#                 # get i'th bit in num
#                 mask = 1 << i               # mask will be something like 0000000100000, 1 being at the i'th position
#                 masked_num = num & mask     # if i'th bit was 0, masked_num is 0. Else masked_num is some number. In this case 100000 = 64
#                 if masked_num is 0:
#                     if not curr.zero:
#                         curr.zero = TrieNode()
#                     curr = curr.zero
#                 else:
#                     if not curr.one:
#                         curr.one = TrieNode()
#                     curr = curr.one
#             curr.value = num

#         max_xor = 0
#         for num in nums:
#             curr = root
#             for i in bit_range:
#                 mask = 1 << i               
#                 masked_num = num & mask  
#                 if masked_num is 0:
#                     if curr.one:
#                         curr = curr.one
#                     else:
#                         curr = curr.zero
#                 else:
#                     if curr.zero:
#                         curr = curr.zero
#                     else:
#                         curr = curr.one
#             max_xor_for_num = num ^ curr.value
#             if max_xor_for_num > max_xor:
#                 max_xor = max_xor_for_num

#         return max_xor
S = Solution()
nums = [3, 10, 5, 25, 2, 8]
print(S.findMaximumXOR(nums))
nums = [0]
print(S.findMaximumXOR(nums))

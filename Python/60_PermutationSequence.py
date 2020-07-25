"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


from functools import lru_cache
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        @lru_cache(None)
        def combs(n):
            if n == 1:
                return n
            return n * combs(n - 1)

        def perm(nums, k):
            if k == 1:
                return nums
            length = len(nums)
            if k == combs(length):
                return nums[::-1]
            step = combs(length-1)
            index = 0
            counts = 0
            while counts + step < k:
                index += 1
                counts += step
            return nums[index] + perm(nums[:index]+nums[index+1:], k - counts)

        str_nums = ''.join(str(i) for i in range(1, n + 1))
        return perm(str_nums, k)

from functools import lru_cache
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        @lru_cache(None)
        def combs(n):
            if n <= 1:
                return 1
            return n * combs(n - 1)

        nums = list(range(1, n+1))
        res = ''
        k -= 1  # index starts from 1 in the question but our list indexs starts from 0
        while n > 0:
            n -= 1
            index, k = divmod(k, combs(n))
            res += str(nums[index])
            nums.pop(index)
        return res

S = Solution()
n = 3
k = 3
print(S.getPermutation(n, k))
n = 4
k = 9
print(S.getPermutation(n, k))
n = 2
k = 2
print(S.getPermutation(n, k))
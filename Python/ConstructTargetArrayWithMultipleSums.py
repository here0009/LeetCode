"""
Given an array of integers target. From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

 

Example 1:

Input: target = [9,3,5]
Output: true
Explanation: Start with [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done
Example 2:

Input: target = [1,1,1,2]
Output: false
Explanation: Impossible to create target array from [1,1,1,1].
Example 3:

Input: target = [8,5]
Output: true
 

Constraints:

N == target.length
1 <= target.length <= 5 * 10^4
1 <= target[i] <= 10^9
"""


import bisect
class Solution:
    def isPossible(self, target) -> bool:
        if len(target) == 1:
            return target.pop() == 1

        target = sorted(target)
        total = sum(target)
        while not all(n == 1 for n in target):
            # print(target)
            num = target.pop()
            rest = total - num
            num2 = num - rest * max(1, num//rest-1)
            # print(num, num2, rest)
            if num2 <= 0:
                return False
            bisect.insort(target, num2)
            total = total - num + num2
        return True


import heapq
class Solution:
    def isPossible(self, target) -> bool:
        total = sum(target)
        target = [-n for n in target]
        heapq.heapify(target)
        while True:
            # print(target)
            num = -heapq.heappop(target)
            total -= num
            if num == 1 or total == 1:
                return True
            if num < total or total == 0 or num % total == 0:
                return False
            num = num % total
            heapq.heappush(target, -num)
            total += num

# https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510338/Python-Replace-reversely-pass-1e911-Priority-Queue
import heapq
class Solution:
    def isPossible(self, A):
        q = [-x for x in A]
        heapq.heapify(q)
        sm = sum(A)
        while True:
            high, rest = -q[0], sm + q[0]
            if high == 1 or rest == 1: return True
            original = high % rest
            if rest >= high or not original: return False
            sm -= high - original
            heapq.heapreplace(q, -original)


S = Solution()
target = [9,3,5]
print(S.isPossible(target))

target = [1,1,1,2]
print(S.isPossible(target))

target = [8,5]
print(S.isPossible(target))

target = [1,1000000000]
print(S.isPossible(target))

target = [2]
print(S.isPossible(target))

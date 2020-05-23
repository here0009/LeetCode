"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
import random
import bisect
class Solution:
    def __init__(self, w):
        self.weights = []
        pre_sum = 0
        for i in w:
            pre_sum += i
            self.weights.append(pre_sum)
        self.sum = pre_sum
        # print(self.weights)

    def pickIndex(self) -> int:
        k = random.randint(1,self.sum)
        # print('k is', k)
        # index = 0
        # while self.weights[index] < k:
        #     index += 1
        # return index
        return bisect.bisect_left(self.weights,k)


class Solution:
    def __init__(self, w):
        self.weights = w
        pre_sum = 0
        for i in range(1,len(self.weights)):
            self.weights[i] += self.weights[i-1]
        self.sum = self.weights[-1]

    def pickIndex(self) -> int:
        k = random.random() * self.sum
        l,r  = 0, len(self.weights)-1
        while l < r:
            mid = (l+r)//2
            if k <= self.weights[mid]:
                r = mid
            else:
                l = mid + 1
        return l

# import random
# class Solution:
#     def __init__(self, w):
#         self.weights = []
#         pre_sum = 0
#         for i in w:
#             pre_sum += i
#             self.weights.append(pre_sum)
#         self.sum = pre_sum
#         print(self.weights)

#     def pickIndex(self) -> int:


# Your Solution object will be instantiated and called as such:


w = [1,3,5,7]
s = Solution(w)
for i in range(10):
    print(s.pickIndex())

# w = [1]
# s = Solution(w)
# for i in range(10):
#     print(s.pickIndex())
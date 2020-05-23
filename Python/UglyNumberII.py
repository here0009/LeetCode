"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
"""
from collections import deque
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2, i3, i5 = 0, 0, 0
        res = [1]
        while len(res) < n:
            while res[i2]*2 <= res[-1]: i2 += 1
            while res[i3]*3 <= res[-1]: i3 += 1
            while res[i5]*5 <= res[-1]: i5 += 1
            res.append(min(res[i2]*2, res[i3]*3, res[i5]*5))

            # print(res)
            # print(i2, i3, i5)
        return res[-1]

class Solution:
    def nthUglyNumber(self, n):
        res = set([1])
        set_a = set([1])
        while len(res) < n:
            set_b = set()
            while set_a:
                tmp = set_a.pop()
                for i in range(2,6):
                    set_b.add(tmp*i)
            res = res | set_b
            set_a = set_b
            print(set_b)
        return sorted(list(res))[n-1]


from collections import deque
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = 1
        curr = 1
        q2 = deque([2])
        q3 = deque([3])
        q5 = deque([5])
        while counts < n:
            curr = min(q2[0],q3[0],q5[0])
            counts += 1
            # print(q2,q3,q5)
            for i,q in (zip([2,3,5],[q2,q3,q5])):
                if q[0] == curr:
                    q.popleft()
                q.append(i*curr)
        return curr
    

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]*n
        p2 = p3 = p5 = 0
        for i in range(1,n):
            # print(nums)
            # print(p2,p3,p5)
            # print(nums[p2]*2, nums[p3]*3, nums[p5]*5)
            nums[i] = min(nums[p2]*2, nums[p3]*3, nums[p5]*5)
            if nums[i] == nums[p2]*2:
                p2 += 1
            if nums[i] == nums[p3]*3:
                p3 += 1
            if nums[i] == nums[p5]*5:
                p5 += 1

        return nums[-1]

s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(1690))
print(s.nthUglyNumber(1))
print(s.nthUglyNumber(13))
"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        """
        TLE
        """
        lst = list(range(1, n + 1))
        step = 1
        while len(lst) > 1:
            # step is odd remove from begin, keep the second
            # step is even remove from end
            # if len(lst) is odd, remove from begin or end are same
            # print(lst)
            if len(lst) % 2 == 1 or step % 2 == 1:
                rmd = 1
            else:
                rmd = 0
            lst = [v for i, v in enumerate(lst) if i % 2 == rmd]
            step += 1
        return lst[0]

# https://leetcode.com/problems/elimination-game/discuss/148451/Easy-Python-3-solution-4-lines
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = range(1, n + 1)
        while len(arr) > 1:
            # print(arr)
            arr = arr[1::2][::-1]
        # print(arr)
        return arr[0]

# https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
class Solution:
    def lastRemaining(self, n):
        left = 1
        head = 1
        step = 1
        remaining = n
        while remaining > 1:
            if left or remaining % 2 == 1:  # either situation we will remove current head
                head += step
            step = step * 2
            left = 1 - left
            remaining //= 2
        return head

S = Solution()
print(S.lastRemaining(9))
print(S.lastRemaining(100))
print(S.lastRemaining(100000000))
# Output
# 86
# Expected
# 54

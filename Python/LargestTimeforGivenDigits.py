"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9
"""
import itertools as it
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        """
        Thoughts: backtracking
        """
        validTime = []
        pmts = it.permutations(A,4)
        for pmt in pmts:
            mins = pmt[0]*10 + pmt[1]
            secs = pmt[2]*10 + pmt[3]
            if mins < 24 and secs < 60:
                validTime.append(mins*100 + secs)
        
        if not validTime:
            return ''
        validTime.sort()
        time_format = "{:0>2}:{:0>2}"
        largestTimeStr = time_format.format(str(validTime[-1]//100) ,str(validTime[-1]%100))
        return largestTimeStr

        # def validTime()

s = Solution()
A = [1,2,3,4]
print(s.largestTimeFromDigits(A))

A = [5,5,5,5]
print(s.largestTimeFromDigits(A))

A = [0,0,0,0]
print(s.largestTimeFromDigits(A))

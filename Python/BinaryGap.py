"""
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:

1 <= N <= 10^9
"""
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_string = "{0:b}".format(N)
        one_positons = list()
        for i in range(len(bin_string)):
            if bin_string[i] == '1':
                one_positons.append(i)
        if len(one_positons) <= 1:
            return 0
        else:
            max_gap = 1
            for i in range(len(one_positons[:-1])):
                gap = one_positons[i+1] - one_positons[i]
                if gap > max_gap:
                    max_gap = gap
        return max_gap

s = Solution()
test = 22
print(s.binaryGap(test))
test = 5
print(s.binaryGap(test))
test = 6
print(s.binaryGap(test))
test = 8
print(s.binaryGap(test))
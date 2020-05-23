"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution:
    def isPowerOfThree(Tself, num: int) -> bool:
        if num <= 0:
            return False
        tmp = 1
        while tmp < num:
            tmp = tmp * 3
        return tmp == num
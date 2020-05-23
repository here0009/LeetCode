"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().

 

Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]
 

Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
 

Follow up:

What is the expected value for the number of calls to rand7() function?
Could you minimize the number of calls to rand7()?
"""
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
"""
Thoughts
rand7()*rand7() will not get uniform 1~49, e.g, prob of 1 is 1/49 , prob of 2 is 2/49, you can not get 13 by rand7()*rand7()
however, we can get uniform 0~48 by (rand7()-1)*7 + rand7()-1, that is (0~6)*7 + (0~6), we wil discard 40~48, and return num//4+1
"""

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            k = (rand7()-1)*7 + rand7()-1
            if k < 40:
                return k//4 + 1
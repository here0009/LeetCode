"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""
class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        invalid_nums = {'3','4','7'}
        num_list = '0125689'
        rotate_list = '0152986'
        rotate_dict = dict()
        for i in range(len(num_list)):
            rotate_dict[(num_list[i])] = rotate_list[i]

        def isValid(n):
            cross_set = set(str(n)) & invalid_nums
            # print("cross_set" ,cross_set)
            if  cross_set:
                return False
            return True

        def rotate(n):
            res = ''
            for num in str(n):
                res += rotate_dict[num]
            return int(res)

        res = 0
        for i in range(1, N+1):
            if isValid(i) and i != rotate(i):
                res += 1
                # print(i, rotate(i))
        return res

class Solution_1:
    """
    Thoughts:
    do not rotate, just do the judgement.
    """
    def rotatedDigits(self, N):
        res = 0
        for i in range(1, N + 1):
            number = str(i)
            if '3' in number or '4' in number or '7' in number:
                continue
            if '2' in number or '5' in number or '6' in number or '9' in number:
                res += 1
        return res

s = Solution()
print(s.rotatedDigits(2))
"""
You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
Example 3:

Input: num = 123456
Output: 820000
Example 4:

Input: num = 10000
Output: 80000
Example 5:

Input: num = 9288
Output: 8700
 

Constraints:

1 <= num <= 10^8
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        """
        wrong answer
        """
        num_list = [int(i) for i in str(num)]
        length = len(num_list)
        if length == 1:
            return 9
        index = 0
        while index < length:
            if num_list[index] != 9:
                break
            index += 1
        max_num = int(''.join([str(i) for i in num_list[:index] + [9] + num_list[index+1:]]))
        if num_list[0] != 1:
            min_num = int(''.join([str(i) for i in [1] + num_list[1:]]))
        else:
            index = 1
            while index < length:
                if num_list[index] != 0:
                    break
                index += 1
            min_num = int(''.join([str(i) for i in num_list[:index] + [0] + num_list[index+1:]]))
        return max_num - min_num


class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        length = len(str_num)

        index = 0
        while index < length:
            if str_num[index] != '9':
                break
            index += 1
        if index == length:
            max_num = int(str_num)
        else:
            max_num = int(str_num.replace(str_num[index], '9'))

        if str_num[0] != '1':
            min_num = int(str_num.replace(str_num[0], '1'))
        else:
            index = 1
            while index < length:
                if str_num[index] != '1' and str_num[index] != '0':
                    break
                index += 1
            if index == length:
                min_num = int(str_num)
            else:
                min_num = int(str_num.replace(str_num[index], '0'))

        # print(num, max_num, min_num)
        return max_num - min_num


class Solution:
    def maxDiff(self, num: int) -> int:
        max_num, min_num = str(num), str(num)
        for d in max_num:
            if d != '9':
                max_num = max_num.replace(d, '9')
                break
        if min_num[0] != '1':
            min_num = min_num.replace(min_num[0], '1')
        else:
            for d in min_num:
                if d not in '01':
                    min_num = min_num.replace(d, '0')
                    break
        return int(max_num) - int(min_num)

S = Solution()
num = 555
print(S.maxDiff(num))
num = 9
print(S.maxDiff(num))
num = 123456
print(S.maxDiff(num))
num = 10000
print(S.maxDiff(num))
num = 9288
print(S.maxDiff(num))
num = 9999
print(S.maxDiff(num))
num = 111
print(S.maxDiff(num))
num = 1101057
print(S.maxDiff(num))
# Output
# 8808000
# Expected
# 8808050
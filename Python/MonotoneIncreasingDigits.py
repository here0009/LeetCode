"""
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""
"""
https://leetcode.com/problems/monotone-increasing-digits/discuss/181945/Fast-and-simple-40ms-Python-solution-using-recursion
"""
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        strN = str(N)
        length = len(strN)
        l = length
        res = int(strN[0])*pow(10,l-1)
        l -= 1
        for i in range(1,length):
            if strN[i] >= strN[i-1]:
                res += int(strN[i])*pow(10,l-1)
            else:
                return self.monotoneIncreasingDigits(res-1)
            l -= 1
        return res

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        e.g. 145732
        """
        nums = [int(i) for i in list(str(N))]
        # print('N',N)
        index, length = 1, len(nums)

        while index < length:
            if nums[index] < nums[index-1]: 
                break
            index += 1

        if index < length:
            while index > 0 and nums[index-1] >= nums[index]: #for nums[index] will minus 1 because of the inversion found above, so it have to be bigger than nums[index-1]
                index -= 1
            nums[index] -= 1 #find the num that should minus 1, others will be repalced with 9
            nums = nums[:index+1] + [9]*(length-index-1)

        return int(''.join([str(i) for i in nums]))


            


S = Solution()
N = 10
print(S.monotoneIncreasingDigits(N))
N = 1234
print(S.monotoneIncreasingDigits(N))
N = 332
print(S.monotoneIncreasingDigits(N))
N = 121
print(S.monotoneIncreasingDigits(N))
N = 145732
print(S.monotoneIncreasingDigits(N))
"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
"""
class Solution:
    def sequentialDigits(self, low: int, high: int):
        str_low = str(low)
        str_high = str(high)
        res = []
        digits = len(str_low)
        digits_high = len(str_high) + 1
        start_num = 0
        while digits < digits_high:
             for start in range(1,10):
                if start + digits <= 10:
                    num = int(''.join([str(i) for i in range(start, start+digits)]))
                    if num >= low and num <= high:
                        res.append(num)
                else:
                    break
             digits += 1
        return res

s = Solution()
low = 100
high = 300
print(s.sequentialDigits(low, high))

low = 1000
high = 13000
print(s.sequentialDigits(low, high))

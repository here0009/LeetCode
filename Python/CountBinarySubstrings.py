"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""
"""
Thoughts
find all the '01' and '10' in s, then expand it if meet the criteria of consecutive numbers.
record the numbers
"""

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def expand(s, left, right):
            counts = 1
            while left > 0 and right < len(s)-1:
                if s[left] == s[left-1] and s[right] == s[right+1]:
                    # print(s[left:right+1])
                    counts += 1
                    left -= 1
                    right += 1
                else:
                    break
            return counts

        res = 0
        p = 0
        while True:
            p = s.find("01", p)
            if p == -1:
                break
            else:
                res += expand(s, p, p+1)
                p += 1

        q = 0
        while q != -1:
            q = s.find("10", q)
            if q == -1:
                break
            else:
                res += expand(s, q, q+1)
                q += 1
        return res



s = Solution()
# test_list = ["00110011"]
test_list = ["00110011", "10101"]
for test in test_list:
    print(s.countBinarySubstrings(test))
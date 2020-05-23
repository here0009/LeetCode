"""
You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.

You are also given an integer maxCost.

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of twith a cost less than or equal to maxCost.

If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to charactor in t, so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You can't make any change, so the maximum length is 1.
 

Constraints:

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s and t only contain lower case English letters.
"""
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        len_s = len(s)
        costs = [0]*len_s
        accCosts = [0]*(len_s+1)
        tmp = 0
        for i in range(len_s):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
            tmp += costs[i]
            accCosts[i+1] = tmp
        # print(costs)
        # print(accCosts)
        start_index = 0
        # end_index = 0
        tmp_cost = 0
        res= 0
        for i in range(1,len_s+1):
            tmp_cost = accCosts[i] - accCosts[start_index]
            while tmp_cost > maxCost:
                start_index += 1
                tmp_cost = accCosts[i] - accCosts[start_index]
            res = max(res, i-start_index)
            # print(start_index)
            # print(res, i, start_index)
        return res


S = Solution()

s = "abcd"
t = "bcdf"
maxCost = 3
print(S.equalSubstring(s,t,maxCost))

s = "abcd"
t = "cdef"
maxCost = 3
print(S.equalSubstring(s,t,maxCost))


s = "abcd"
t = "acde"
maxCost = 0
print(S.equalSubstring(s,t,maxCost))

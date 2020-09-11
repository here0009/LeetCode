"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

 

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
 

Constraints:

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s contains only lowercase English letters.
"""


class Solution:
    def minCost(self, s: str, cost) -> int:
        length = len(cost)
        pre_letter, pre_score = s[0], cost[0]
        res = 0
        for i in range(1, length):

            if s[i] == pre_letter:
                res += min(cost[i], pre_score)
                pre_score = max(pre_score, cost[i])
            else:
                pre_letter, pre_score = s[i], cost[i]
            # print(s[i], cost[i], res)
        return res


class Solution:
    def minCost(self, s, cost):
        res = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res

S = Solution()
s = "abaac"
cost = [1,2,3,4,5]
print(S.minCost(s, cost))
s = "abc"
cost = [1,2,3]
print(S.minCost(s, cost))
s = "aabaa"
cost = [1,2,3,4,1]
print(S.minCost(s, cost))
s = "aaabbbabbbb"
cost = [3,5,10,7,5,3,5,5,4,8,1]
print(S.minCost(s, cost))
# Output:
# 25
# Expected:
# 26
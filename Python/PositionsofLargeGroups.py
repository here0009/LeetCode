"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
 

Note:  1 <= S.length <= 1000
"""
class Solution_1:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res = []
        if len(S) < 3:
            return res
        pre = S[0]
        cst_num = 1
        for i in range(1,len(S)):
            if S[i] == pre:
                cst_num += 1
                # print(i, S[i], cst_num)
                if i == len(S)-1 and cst_num >= 3:
                    res.append([i-cst_num+1, i])
            else:
                pre = S[i]
                if cst_num >= 3:
                    res.append([i-cst_num, i-1])
                cst_num = 1
        return res

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start = 0
        i = 0
        res = []
        while i < len(S):
            while i < len(S) and S[i] == S[start]:
                i += 1
            end = i - 1
            if end - start >=2 :
                res.append([start, end])
            start = i
        return res

s = Solution()
S = "abbxxxxzzy"
print(s.largeGroupPositions(S))

S = "abc"
print(s.largeGroupPositions(S))

S = "abcdddeeeeaabbbcd"
print(s.largeGroupPositions(S))

S = "aaa"
print(s.largeGroupPositions(S))
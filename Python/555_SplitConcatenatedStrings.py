"""
Given a list of strings, you could concatenate these strings together into a loop, where for each string you could choose to reverse it or not. Among all the possible loops, you need to find the lexicographically biggest string after cutting the loop, which will make the looped string into a regular one.

Specifically, to find the lexicographically biggest string, you need to experience two phases:

Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.
Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.
And your job is to find the lexicographically biggest one among all the possible regular strings.

Example:
Input: "abc", "xyz"
Output: "zyxcba"
Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", 
where '-' represents the looped status. 
The answer string came from the fourth looped one, 
where you could cut from the middle character 'a' and get "zyxcba".
Note:
The input strings will only contain lowercase letters.
The total length of all the strings will not over 1,000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-concatenated-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# https://leetcode-cn.com/problems/split-concatenated-strings/solution/fen-ge-lian-jie-zi-fu-chuan-by-leetcode-solution/
class Solution:
    def splitLoopedString(self, strs) -> str:
        strs = [s[::-1] if s[::-1] > s else s for s in strs]
        res = ''.join(strs)
        for i in range(len(strs)):
            string = strs[i]  # split string in middle
            rev_string = string[::-1]
            others = ''.join(strs[i+1:]) + ''.join(strs[:i])
            for j in range(len(string)):
                s1 = string[j:] + others + string[:j]
                s2 = rev_string[j:] + others + rev_string[:j]
                res = max(res, s1, s2)
        return res


S = Solution()
strs = ["xyz", "abc", "xyz", "abc"]
print(S.splitLoopedString(strs))
strs = ['z', 'b', 'z', 'a']
print(S.splitLoopedString(strs))
strs = ["abc", "xyz"]
print(S.splitLoopedString(strs))
strs = ["lc","evol","cdy"]
print(S.splitLoopedString(strs))
# 输出：
# "ydclclove"
# 预期结果：
# "ylclovecd"
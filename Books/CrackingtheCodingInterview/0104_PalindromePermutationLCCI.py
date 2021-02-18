"""
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

 

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odds = len(s) % 2
        counts = Counter(s)
        tmp = 0
        for v in counts.values():
            tmp += v % 2
            if tmp > odds:
                return False
        return True


S = Solution()
s = "tactcoa"
print(S.canPermutePalindrome(s))
s = "tactco"
print(S.canPermutePalindrome(s))
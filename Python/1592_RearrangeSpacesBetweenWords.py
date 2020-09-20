"""
给你一个字符串 text ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 text 至少包含一个单词 。

请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化 该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾 ，这也意味着返回的字符串应当与原 text 字符串的长度相等。

返回 重新排列空格后的字符串 。

 

示例 1：

输入：text = "  this   is  a sentence "
输出："this   is   a   sentence"
解释：总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。
示例 2：

输入：text = " practice   makes   perfect"
输出："practice   makes   perfect "
解释：总共有 7 个空格和 3 个单词。7 / (3-1) = 3 个空格加上 1 个多余的空格。多余的空格需要放在字符串的末尾。
示例 3：

输入：text = "hello   world"
输出："hello   world"
示例 4：

输入：text = "  walks  udp package   into  bar a"
输出："walks  udp  package  into  bar  a "
示例 5：

输入：text = "a"
输出："a"
 

提示：

1 <= text.length <= 100
text 由小写英文字母和 ' ' 组成
text 中至少包含一个单词

You are given a string text of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned string should be the same length as text.

Return the string after rearranging the spaces.

 

Example 1:

Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
Example 2:

Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
Example 3:

Input: text = "hello   world"
Output: "hello   world"
Example 4:

Input: text = "  walks  udp package   into  bar a"
Output: "walks  udp  package  into  bar  a "
Example 5:

Input: text = "a"
Output: "a"
 

Constraints:

1 <= text.length <= 100
text consists of lowercase English letters and ' '.
text contains at least one word.
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = sum([1 for w in text if w == ' '])
        if len(words) == 1:
            return words[0]+' '*spaces
        d, r = divmod(spaces, len(words)-1)
        # print(d,r)
        return (' '*d).join(words) + ' '*r

S = Solution()
text = "  this   is  a sentence "
print(S.reorderSpaces(text))
text = " practice   makes   perfect"
print(S.reorderSpaces(text))
text = "hello   world"
print(S.reorderSpaces(text))
text = "  walks  udp package   into  bar a"
print(S.reorderSpaces(text))
text = "a"
print(S.reorderSpaces(text))
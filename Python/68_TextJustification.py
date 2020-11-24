"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/text-justification
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def fullJustify(self, words, maxWidth: int):
        def justify(line, len_line):
            extra_space = maxWidth - len_line
            if len(line) == 1:
                return line[0] + ' '*extra_space
            d, rmd = divmod(extra_space, len(line)-1)
            res = line[0]
            for i in range(1, len(line)):
                if i <= rmd:
                    res += (d+1)*' ' + line[i]
                else:
                    res += d*' ' + line[i]
            return res

        res = []
        index = 0
        length = len(words)
        line = []
        len_line = 0
        while index < length:
            word = words[index]
            if len_line + len(line) + len(word) <= maxWidth:
                len_line += len(word)
                line.append(word)
            else:
                res.append(justify(line, len_line))
                line = [word]
                len_line = len(word)
            index += 1

        last_line = ' '.join(line)
        if last_line:
            res.append(last_line + ' '*(maxWidth - len(last_line)))
        # for row in res:
        #     print(row)
        return res

S = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(S.fullJustify(words, maxWidth))
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(S.fullJustify(words, maxWidth))
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
print(S.fullJustify(words, maxWidth))

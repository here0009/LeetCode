"""
Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.
Valid Code Examples:
Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

Output: True

Explanation: 

The code is wrapped in a closed tag : <DIV> and </DIV>. 

The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 

Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

So TAG_CONTENT is valid, and then the code is valid. Thus return true.


Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

Output: True

Explanation:

We first separate the code into : start_tag|tag_content|end_tag.

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content could also be separated into : text1|cdata|text2.

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

text2 -> "]]>>]"


The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
Invalid Code Examples:
Input: "<A>  <B> </A>   </B>"
Output: False
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

Input: "<DIV>  div tag is not closed  <DIV>"
Output: False

Input: "<DIV>  unmatched <  </DIV>"
Output: False

Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
Output: False

Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
Output: False

Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
Output: False
Note:
For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '<','>','/','!','[',']' and ' '.

"""
# https://leetcode.com/problems/tag-validator/discuss/279586/Python-One-pass-leveraging-State-Machine
# https://leetcode.com/problems/tag-validator/discuss/103370/Short-Python-accepted-but-not-sure-if-correct
# https://leetcode.com/problems/tag-validator/discuss/103380/Python-Straightforward-with-Explanation


class Solution:
    def isValid(self, code: str) -> bool:
        """
        Thoughts:
        1. check if tag name is valid
        2. chekc if tag content is valid
        3. use a stack to store open tag, use end tag to pop from stack
        """
        def parse_tag(i: int) -> str:
            j = i + 1
            while j < len_code and code[j] != '>':
                j += 1
            return code[i: j + 1] if j != len_code else None

        def parse_cdata(i: int) -> str:
            if not code[i:].startswith(cdata_start):
                return None
            j = code.find(cdata_end, i)
            if j == -1:
                return None
            print('cdata', code[i: j + 3])
            return code[i: j + 3]

        def check_tag(tag: str) -> bool:
            print(tag)
            """
            -1 : not valid
            0: cdata
            1: end tag
            2: start tag
            """
            if not tag or tag[0] != '<':
                return False
            close_flag = False
            if tag.startswith('</'):
                close_flag = True
            tag_name = tag[1 + close_flag: -1]
            print(tag_name, 'clostag', close_flag)
            # print(not all('A' <= c <= 'Z' for c in tag_name))
            if (not 0 < len(tag_name) < 10) or not all('A' <= c <= 'Z' for c in tag_name):
                return False
            if not close_flag:
                stack.append(tag_name)
                print(stack)
                return True
            if close_flag:
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                return True

        stack = []
        cdata_start = '<![CDATA['
        cdata_end = ']]>'
        len_code = len(code)
        idx = 0
        tag = parse_tag(idx)
        if tag is None or not check_tag(tag):
            return False
        idx += len(tag)
        print(idx)
        while idx < len_code:
            c = code[idx]
            print(c, idx)
            if c == '<':
                print(code[idx: idx + 2])
                if code[idx: idx + 2] == '<!':
                    tag = parse_cdata(idx)
                    if tag is None:
                        return False
                else:
                    tag = parse_tag(idx)
                    if tag is None or not check_tag(tag):
                        print('tag', tag, check_tag(tag))
                        return False
                idx += len(tag)
            else:
                idx += 1
        return len(stack) == 0


class Solution:
    def isValid(self, code: str) -> bool:
        """
        Thoughts:
        1. check if tag name is valid
        2. chekc if tag content is valid
        3. use a stack to store open tag, use end tag to pop from stack
        """
        def parse_tag(i: int) -> int:
            j = i + 1
            while j < len_code and code[j] != '>':
                j += 1
            return j + 1 if j != len_code else -1

        def parse_cdata(i: int) -> int:
            if not code[i:].startswith(cdata_start):
                return -1
            j = code.find(cdata_end, i)
            if j == -1:
                return -1
            return j + 3

        def check_tag(idx, end_idx) -> bool:
            tag = code[idx: end_idx]
            if not tag or tag[0] != '<':
                return False
            close_flag = False
            if tag.startswith('</'):
                close_flag = True
            tag_name = tag[1 + close_flag: -1]
            if (not 0 < len(tag_name) < 10) or not all('A' <= c <= 'Z' for c in tag_name):
                return False
            if not close_flag:
                stack.append((tag_name, end_idx))
                return True
            if close_flag:
                if not stack or stack[-1][0] != tag_name:
                    # no corresponding start or no content
                    return False
                stack.pop()
                return True

        stack = []
        cdata_start = '<![CDATA['
        cdata_end = ']]>'
        len_code = len(code)
        idx = 0
        end_idx = parse_tag(idx)
        if end_idx == -1 or not check_tag(idx, end_idx) or not code.endswith('</' + code[idx + 1: end_idx]):
            return False
        idx = end_idx
        while idx < len_code:
            c = code[idx]
            if c == '<':
                if code[idx: idx + 2] == '<!':
                    end_idx = parse_cdata(idx)
                    if end_idx == -1:
                        return False
                else:
                    end_idx = parse_tag(idx)
                    if end_idx == -1 or not check_tag(idx, end_idx):
                        return False
                idx = end_idx
            else:
                idx += 1
        return len(stack) == 0


import re
class Solution:
    def isValid(self, code):

        print(code)
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        print(code)
        pre = None
        while pre != code:
            pre = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
            print(code)
        print('+++++++++++++++++++++')
        return code == 't'


S = Solution()
code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
print(S.isValid(code))
code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
print(S.isValid(code))
code = "<A>  <B> </A>   </B>"
print(S.isValid(code))
code = "<DIV>  div tag is not closed  <DIV>"
print(S.isValid(code))
code = "<DIV>  unmatched <  </DIV>"
print(S.isValid(code))
code = "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
print(S.isValid(code))
code = "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
print(S.isValid(code))
code = "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
print(S.isValid(code))
code = "<A></A><B></B>"  # the whole array shoule be one tag so must be <A>....</A>
print(S.isValid(code))
# Output
# true
# Expected
# false
code = "<A><A>/A></A></A>"
print(S.isValid(code))
code = "<A><A></A></A>"
print(S.isValid(code))

"""
Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

Each a_i is a non-empty string;
Their concatenation a_1 + a_2 + ... + a_k is equal to text;
For all 1 <= i <= k,  a_i = a_{k+1 - i}.
 

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
Example 4:

Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".
 

Constraints:

text consists only of lowercase English characters.
1 <= text.length <= 1000
"""

class Solution:
    def longestDecomposition(self, text: str) -> int:
        # print(res)
        # print('text2',text2)
        # print('striped',text2[:length])

        if end_pos == -1 or end_pos == 0 or text2[:length] != text2[end_pos:]:
            res += 1
            text2 = ''
        else:
            res += 2
            text2 = text2[length:end_pos]

from collections import defaultdict
from collections import deque
class Solution:
    def longestDecomposition(self, text: str) -> int:
        pos_dict = defaultdict(deque)
        for i,v in enumerate(text):
            pos_dict[v].append(i)
        res = 0
        text2 = text
        left_index, right_index = 0, len(text2)
        while left_index < right_index:
            left_letter = text2[left_index]
            pos_list = pos_dict[left_letter]
            while pos_list and pos_list[-1] < left_index:
                pos_list.popleft() #left_index
            found = False
            while pos_list and pos_list[-1] > right_index:
                pos_list.pop()
            while pos_list:
                right_pos = pos_list.pop()
                length = right_index-right_pos
                # print('left', text2[left_index:left_index+length])
                # print('right',text2[right_pos:right_index])
                if text2[left_index:left_index+length] == text2[right_pos:right_index]:
                    found = True
                    if left_index == right_pos:
                        res += 1
                        return res
                    else:
                        res += 2
                    left_index += length
                    right_index -= length
                    break
        return res

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        if n == 0:
            return 0
        for i in range(n//2+1):
            if text[:i] == text[-i:]:
                return 2+self.longestDecomposition(text[i:-i])
        return 1

S = Solution()
text = "ghiabcdefhelloadamhelloabcdefghi"
print(S.longestDecomposition(text))
text = "merchant"
print(S.longestDecomposition(text))
text = "antaprezatepzapreanta"
print(S.longestDecomposition(text))
text = "aaa"
print(S.longestDecomposition(text))
text = "elvtoelvto"
print(S.longestDecomposition(text))
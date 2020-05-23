"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
 

Note:

1 <= paragraph.length <= 1000.
1 <= banned.length <= 100.
1 <= banned[i].length <= 10.
The answer is unique, and written in lowercase (even if its occurrences in paragraph may have uppercase symbols, and even if it is a proper noun.)
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
There are no hyphens or hyphenated words.
Words only consist of letters, never apostrophes or other punctuation symbols.
"""
from collections import Counter
import string
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        for c in string.punctuation:
            paragraph = paragraph.replace(c, ' ')
        # paragraph_list = re.split(',| |;|-',paragraph)
        # paragraph_list = [word.lower() for word in paragraph_list]
        paragraph_list = [word.lower() for word in re.split(r'\s+',paragraph)]
        # print(paragraph_list)
        p_counter = Counter(paragraph_list)
        
        max_v = 0
        max_k = paragraph_list[0]
        # print(p_counter)
        for k,v in p_counter.items():
            if v > max_v and k not in banned:
                max_v = v
                max_k = k
        return max_k

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(s.mostCommonWord(paragraph,banned))

paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
print(s.mostCommonWord(paragraph,banned))
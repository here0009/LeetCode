"""
Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a lengthy document. A sentence like "I reset the computer. It still didn't boot!" became "iresetthecomputeritstilldidntboot''. You'll deal with the punctuation and capi­talization later; right now you need to re-insert the spaces. Most of the words are in a dictionary but a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm to unconcatenate the document in a way that minimizes the number of unrecognized characters. Return the number of unrecognized characters.

Note: This problem is slightly different from the original one in the book.

 

Example:

Input: 
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
Output:  7
Explanation:  After unconcatenating, we got "jess looked just like tim her brother", which containing 7 unrecognized characters.
Note:

0 <= len(sentence) <= 1000
The total number of characters in dictionary is less than or equal to 150000.
There are only lowercase letters in dictionary and sentence.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/re-space-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from functools import lru_cache
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:

        @lru_cache(None)
        def split_word(string):
            cost = len(string)
            for i in range(1, len(string) + 1):
                tmp_cost = split_word(string[i:])
                if string[:i] not in dict_set:
                    tmp_cost += i
                cost = min(tmp_cost, cost)
            # print(string, cost)
            return cost

        dict_set = set(dictionary)
        # print(dict_set)
        return split_word(sentence)

S = Solution()
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
# sentence = "er"
print(S.respace(dictionary, sentence))

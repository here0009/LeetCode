"""
can not use set during the contest
Line 60: Exception: Type <class 'set'>: Not implemented
"""
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_words_set = set(A.split(' '))
        b_words_set = set(B.split(' '))
        unique_words = a_words_set.symmetric_difference(b_words_set)
        # print(a_words_set)
        # print(b_words_set)
        # print(unique_words)
        return unique_words

s = Solution()
A = "this apple is sweet"
B = "this apple is sour"
print(s.uncommonFromSentences(A, B))

A = "apple apple"
B = "banana"
print(s.uncommonFromSentences(A, B))
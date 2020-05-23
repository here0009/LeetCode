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
        a_words = A.split(' ')
        b_words = B.split(' ')
        a_words_dict = dict()
        unique_words = list()
        a_words.extend(b_words)

        for word in a_words:
            if word in a_words_dict:
                a_words_dict[word] = 0
            else:
                a_words_dict[word] = 1

        for word, value in a_words_dict.items():
            if value == 1:
                unique_words.append(word)

        return unique_words

s = Solution()
A = "this apple is sweet"
B = "this apple is sour"
print(s.uncommonFromSentences(A, B))

A = "apple apple"
B = "banana"
print(s.uncommonFromSentences(A, B))
"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

 

Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false
Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
Example 4:

Input: sentence1 = "Luky", sentence2 = "Lucccky"
Output: false
 

Constraints:

1 <= sentence1.length, sentence2.length <= 100
sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
The words in sentence1 and sentence2 are separated by a single space.
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 < len_s2:
            s1, s2 = s2, s1
            len_s1, len_s2 = len_s2, len_s1
        # print(s1)
        # print(s2)
        left, right_2, right_1 = 0, len_s2 - 1, len_s1 - 1
        while left < len_s2 and s1[left] == s2[left]:
            left += 1
        # print(left)
        # if left == len_s2:
        #     return True
        while right_2 >= left and s2[right_2] == s1[right_1]:
            right_2 -= 1
            right_1 -= 1
        # print(left, right_2)
        return left - right_2 == 1

S = Solution()

sentence1 = "My name is Haley"
sentence2 = "My Haley"
print(S.areSentencesSimilar(sentence1, sentence2))
sentence1 = "of"
sentence2 = "A lot of words"
print(S.areSentencesSimilar(sentence1, sentence2))
sentence1 = "Eating right now"
sentence2 = "Eating"
print(S.areSentencesSimilar(sentence1, sentence2))
sentence1 = "Luky"
sentence2 = "Lucccky"
print(S.areSentencesSimilar(sentence1, sentence2))
sentence1 = "Ogn WtWj HneS"
sentence2 ="Ogn WtWj HneS"
print(S.areSentencesSimilar(sentence1, sentence2))

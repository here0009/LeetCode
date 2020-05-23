"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""
class Solution:
    def expressiveWords(self, S: str, words) -> int:
        def word_to_list(word):
            if not word:
                return []
            res = []
            pre = word[0]
            counts = 1
            for letter in word[1:]:
                if letter == pre:
                    counts +=1
                else:
                    res.append((pre,counts))
                    pre = letter
                    counts = 1
            res.append((pre,counts))
            return res


        S_list = word_to_list(S)
        len_S_list = len(S_list)
        # print(S_list)
        res = 0
        for word in words:
            word_list = word_to_list(word)
            # print(word_list)
            if len(word_list) != len(S_list):
                continue
            break_flag = False
            for i in range(len_S_list):
                if S_list[i][0] != word_list[i][0] or not (S_list[i][1] == word_list[i][1] or (word_list[i][1] < S_list[i][1] and S_list[i][1] >= 3)):
                    break_flag = True
                    break
            if not break_flag:
                res += 1
        return res


class Solution:
    def expressiveWords(self, S: str, words) -> int:
        def check(S,word):
            i,j,i2,j2,m,n = 0,0,0,0,len(S),len(word)
            while i<m and j<n:
                if S[i] != word[j]:
                    return False
                while i2< m and S[i2] == S[i]: i2+= 1
                while j2< n and word[j2] == word[j]: j2+=1
                if i2-i != j2-j and i2 -i  < max(3, j2-j):
                    return False
                i,j = i2,j2
            return i == m and j == n

        return sum([check(S,word) for word in words])


s = Solution()
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# print(s.expressiveWords(S, words))


S = "dddiiiinnssssssoooo"
words = ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
print(s.expressiveWords(S, words))

S = "aaa"
words = ["aaaa"]
print(s.expressiveWords(S, words))
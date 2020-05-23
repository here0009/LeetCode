"""
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

 

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
Example 2:

Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.
Example 3:

Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.
 

Constraints:

1 <= words.length <= 14
1 <= words[i].length <= 15
1 <= letters.length <= 100
letters[i].length == 1
score.length == 26
0 <= score[i] <= 10
words[i], letters[i] contains only lower case English letters.
"""
"""
claculate the situation using word[i] or not using word[i]
"""
from collections import Counter
class Solution_1:
    def maxScoreWords(self, words, letters, score) -> int:
        """
        TLE, no need to use visited, can just record the visited index, and visit other node since then
        """
        
        def dfs(counter, score, vis):
            for index,word in enumerate(words):
                if vis[index] == 1:
                    continue
                tmp_counter = {k:v for k,v in counter.items()}
                w_counter = w_counter_list[index]
                tmp_vis = vis[:]
                for k,v in w_counter.items():
                    if k not in tmp_counter or tmp_counter[k] < w_counter[k]:
                        break
                    else:
                        tmp_counter[k] -= w_counter[k]
                else:
                    tmp_score = score + score_dict[word]
                    tmp_vis[index] = 1
                    # print(tmp_counter,word,score,tmp_score)
                    self.res = max(self.res, tmp_score) 
                    dfs(tmp_counter, tmp_score,tmp_vis)


        w_counter_list = [Counter(word) for word in words]
        visited = len(words)*[0]
        score_dict = dict()
        for word in words:
            score_dict[word] = sum([score[ord(letter)-ord('a')] for letter in word])

        l_counter = Counter(letters)
        # print(l_counter)
        # print(w_counter_list)
        # print(score_dict)
        self.res = 0
        dfs(l_counter,0,visited)

        return self.res


from collections import Counter
class Solution_2:
    def maxScoreWords(self, words, letters, score) -> int:
        def dfs(index,counter, score):
            for j in range(index, len_w):
                tmp_counter = {k:v for k,v in counter.items()}
                w_counter = w_counter_list[j]
                for k,v in w_counter.items():
                    if k not in tmp_counter or tmp_counter[k] < w_counter[k]:
                        break
                    else:
                        tmp_counter[k] -= w_counter[k]
                else:
                    tmp_score = score + score_dict[words[j]]
                    # print(tmp_counter,word,score,tmp_score)
                    self.res = max(self.res, tmp_score) 
                    dfs(j+1, tmp_counter, tmp_score)


        w_counter_list = [Counter(word) for word in words]
        len_w = len(words)
        score_dict = dict()
        for word in words:
            score_dict[word] = sum([score[ord(letter)-ord('a')] for letter in word])

        l_counter = Counter(letters)
        self.res = 0
        dfs(0,l_counter,0)

        return self.res

from collections import Counter
class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        def dfs(index,counter,score):
            # print(index, counter,score)
            for j in range(index, len_w):
                w_counter = w_counter_list[j]
                if all([v<=counter.get(k,0) for k,v in w_counter.items()]):
                    tmp_score = score + score_dict[words[j]]
                    self.res = max(self.res, tmp_score) 
                    dfs(j+1, {k:v-w_counter.get(k,0) for k,v in counter.items()}, tmp_score)


        w_counter_list = [Counter(word) for word in words]
        len_w = len(words)
        score_dict = dict()
        for word in words:
            score_dict[word] = sum([score[ord(letter)-ord('a')] for letter in word])

        l_counter = Counter(letters)
        self.res = 0
        dfs(0,l_counter,0)

        return self.res

S = Solution()
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(S.maxScoreWords(words, letters, score))
words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
print(S.maxScoreWords(words, letters, score))
words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
print(S.maxScoreWords(words, letters, score))

words =["add","dda","bb","ba","add"]
letters = ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"]
score = [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(S.maxScoreWords(words, letters, score))

words =["bhtgqlbhbko","emnnd","seilhhmjatngm","tjjpempmhioeakm","tpmicqabgpbdmkl","pbfpg","ajjpeojacckgl","pcssptkteqi","mieolfbmjkb","eqshjsiq","kqnfgl","sqmcmsm","ttktnasfktfdr","ddmpgoq"]
letters = ["a","b","b","b","b","c","c","c","d","d","d","d","d","e","e","e","e","e","e","f","f","f","f","f","g","g","g","g","g","h","h","h","h","i","i","i","j","j","j","j","k","k","l","l","l","l","l","l","l","m","m","n","n","n","o","p","p","p","p","p","p","q","q","q","q","q","q","r","s","s","s","t","t","t","t","t"]
score =[2,6,3,7,5,9,4,4,8,1,6,9,1,1,1,1,7,5,2,5,0,0,0,0,0,0]
print(S.maxScoreWords(words, letters, score))


words =["cdab","ad","ddd","cbc","ac","db"]
letters = ["a","a","a","a","b","b","b","c","c","c","c","c","c","d","d","d"]
score =[10,2,5,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(S.maxScoreWords(words, letters, score))
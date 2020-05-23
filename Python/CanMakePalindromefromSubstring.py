"""
Given a string s, we make queries on substrings of s.

For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right], and then choose up to k of them to replace with any lowercase English letter. 

If the substring is possible to be a palindrome string after the operations above, the result of the query is true. Otherwise, the result is false.

Return an array answer[], where answer[i] is the result of the i-th query queries[i].

Note that: Each letter is counted individually for replacement so if for example s[left..right] = "aaa", and k = 2, we can only replace two of the letters.  (Also, note that the initial string s is never modified by any query.)

 

Example :

Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0] : substring = "d", is palidrome.
queries[1] : substring = "bc", is not palidrome.
queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.
 

Constraints:

1 <= s.length, queries.length <= 10^5
0 <= queries[i][0] <= queries[i][1] < s.length
0 <= queries[i][2] <= s.length
s only contains lowercase English letters.
"""
# from collections import 
class Solution_1:
    """
    TLE
    try to use a dict to store the information
    """

    def canMakePaliQueries(self, string, queries):
        def unPnum(start,end):
            """
            return the nonPalidrome letters in string
            """
            letters = set()
            for i in range(start, end+1):
                s = string[i]
                if s not in letters:
                    letters.add(s)
                else:
                    letters.remove(s)
            # print(letters)
            return (len(letters)-1)/2
            # return res

        res = []
        for left, right, k in queries:
            n = unPnum(left, right)
            if n <= k:
                res.append(True)
            else:
                res.append(False)
        return res

from collections import Counter
class Solution:
    """
    still TLE
    """
    def canMakePaliQueries(self, string, queries):
        def unPnum(start,end):
            # diff = Counter(end) - Counter(start)
            diff_num = 0
            end_dict = counters[end+1]
            start_dict = counters[start]
            # print(start_dict, end_dict)
            for key,value in end_dict.items():
                v = value - start_dict.get(key,0)
                if v % 2 == 1:
                    diff_num += 1
            # print(diff_num)
            return (diff_num-1)/2


        counters = []
        for i in range(len(string)+1):
            counters.append(Counter(string[:i]))
        # print(counters)
        res = []
        for left, right, k in queries:
            n = unPnum(left, right)
            if n <= k:
                res.append(True)
            else:
                res.append(False)
        return res

s = Solution()
string = "abcda"
queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
print(s.canMakePaliQueries(string, queries))

string = "hunu"
queries = [[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]]
print(s.canMakePaliQueries(string, queries))

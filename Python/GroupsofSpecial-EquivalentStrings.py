"""
You are given an array A of strings.

Two strings S and T are special-equivalent if after any number of moves, S == T.

A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].

Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from A.

 

Example 1:

Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Example 2:

Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]

Example 3:

Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]

Example 4:

Input: ["abcd","cdab","adcb","cbad"]
Output: 1
Explanation: 1 group ["abcd","cdab","adcb","cbad"]
 

Note:

1 <= A.length <= 1000
1 <= A[i].length <= 20
All A[i] have the same length.
All A[i] consist of only lowercase letters.
"""
class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        dict_string_set = set()
        res = 0
        for string in A:
            odd_counts = dict()
            even_counts = dict()
            for i in range(len(string)):
                if i%2:
                    odd_counts[string[i]] = odd_counts.get(string[i], 0) + 1
                else:
                    even_counts[string[i]] = even_counts.get(string[i], 0) + 1
            dict_string = self.dictToString(even_counts, odd_counts)
            # print(dict_string)
            if dict_string not in dict_string_set:
                dict_string_set.add(dict_string)

        return len(dict_string_set)
    def dictToString(self, dict_left, dict_right):
        """
        Use a string to represent the elemnts of dict_left and dict_right
        """
        res = 'L'
        for key in sorted(dict_left.keys()):
            res += key + str(dict_left[key])
        res += 'R'
        for key in sorted(dict_right.keys()):
            res += key + str(dict_right[key])
        return res


class Solution_1:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res_set = set()
        for string in A:
            odd_letter = ''.join(list(sorted(string[0::2])))
            if len(string) > 1:
                even_letter = ''.join(list(sorted(string[1::2])))
            else:
                even_letter = ''
            letter = odd_letter + ' ' + even_letter
            res_set.add(letter)
        return len(res_set)

class Solution_2:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res_set = set()
        for string in A:
            odd_letter = ''.join(list(sorted(string[0::2])))
            even_letter = ''.join(list(sorted(string[1::2])))
            #when a list or string is sliced using [a:b:c], a, b, c can be any number.
            #they do not have to be in the range of len(string) or len(list)
            #but if you want to get the value of string[a], you have to make sure that a in range(len(string))
            letter = odd_letter + ' ' + even_letter
            res_set.add(letter)
        return len(res_set)     

s = Solution_2()

test = ["a","b","c","a","c","c"]
print(s.numSpecialEquivGroups(test))

test = ["aa","bb","ab","ba"]
print(s.numSpecialEquivGroups(test))

test = ["abc","acb","bac","bca","cab","cba"]
print(s.numSpecialEquivGroups(test))

test = ["abcd","cdab","adcb","cbad"]
print(s.numSpecialEquivGroups(test))

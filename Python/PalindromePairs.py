"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""
class Solution_1:
    """
    TLE
    """
    def palindromePairs(self, words):
        def isPalindrome(string):
            start, end = 0, len(string)-1
            while start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True

        res = []
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if len(words[i]) == 0 and len(words[j]) == 0:
                    continue
                elif len(words[i]) == 0 or len(words[j]) == 0:
                    if isPalindrome(words[i]+words[j]):
                        res.append([i,j])
                        res.append([j,i])                   
                else:
                    si,ei = words[i][0], words[i][-1]
                    sj,ej = words[j][0], words[j][-1]
                    if si == ej:
                        if isPalindrome(words[i]+words[j]):
                            res.append([i,j])
                    if sj == ei:
                        if isPalindrome(words[j]+words[i]):
                            res.append([j,i])
        return res



class Solution:
    """
    use rev_dict to record the reverse words, if split the word to left and right part based on diff index
    if left is palindrome and right in rev_dict(the index is i, i is not equal to the index of the word), then rev_dict[i]+left+right
    similarly, if right is palindrome and lef in rev_dict, then left+right+rev_dict[i] is palindrome
    """
    def palindromePairs(self, words):
        def isPalindrome(string):
            return string == string[::-1]

        rev_dict = {word[::-1]:i for i,word in enumerate(words)}
        # print(rev_dict)
        res = set()
        for index, word in enumerate(words):
            for j in range(len(word)+1):
                left = word[:j]
                right = word[j:]
                # print(word,left,right)
                if isPalindrome(left) and (right in rev_dict) and (rev_dict[right] != index):
                    res.add((rev_dict[right], index))
                if isPalindrome(right) and (left in rev_dict) and (rev_dict[left] != index):
                    res.add((index, rev_dict[left]))
        return [list(t) for t in res]


s = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(s.palindromePairs(words))

words = ["bat","tab","cat"]
print(s.palindromePairs(words))

words = ["a",""]
print(s.palindromePairs(words))

words = ["a","abc","aba",""]
print(s.palindromePairs(words))
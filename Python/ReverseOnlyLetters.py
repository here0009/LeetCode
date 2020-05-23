"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \\ or "
"""
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        start_index = 0
        end_index = len(S)-1
        res_list = list(S)
        while True:
            
            while start_index < len(S)-1:
                if self.isLetter(res_list[start_index]):
                    break
                else:
                    start_index += 1
                
            while end_index > 0:
                if self.isLetter(res_list[end_index]):
                    break
                else:
                    end_index -= 1
                
            if start_index < end_index:
                tmp = res_list[start_index]
                res_list[start_index] = res_list[end_index]
                res_list[end_index] = tmp
                start_index += 1
                end_index -= 1
            else:
                break

        return ''.join(res_list)


    def isLetter(self, s):
        if (s >= 'a' and s <= 'z') or (s >= 'A' and s <= 'Z'):
            return True
        else:
            return False

class Solution_2:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        """
        Thoughts: Solution_2 is more elegant
        """
        new = []
        letters = [c for c in S if c.isalpha()]
        for i in range(len(S)):
            if S[i].isalpha():
                new.append(letters.pop())
            else:
                new.append(S[i])
        res = ''.join(str(v) for v in new)
        return res

s = Solution()
# print(s.isLetter('a'))
# print(s.isLetter('b'))
# print(s.isLetter('X'))
# print(s.isLetter('='))
print(s.reverseOnlyLetters("ab-cd"))
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(s.reverseOnlyLetters("7_28]"))

"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
Note:

1 <= S.length = shifts.length <= 20000
0 <= shifts[i] <= 10 ^ 9
"""
class Solution:
    def shiftingLetters(self, string: str, shifts) -> str:
        acc_shifts = shifts[:]
        for i in range(len(shifts)-2,-1,-1):
            acc_shifts[i] += acc_shifts[i+1]
        # print(acc_shifts)
        res = ''
        for i in range(len(string)):
            res += chr((ord(string[i])+acc_shifts[i]-ord('a'))%26 + ord('a'))
        return res

S = Solution()
string = "abc"
shifts = [3,5,9]
print(S.shiftingLetters(string, shifts))

string = "a"
shifts = [3]
print(S.shiftingLetters(string, shifts))
"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""
class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        letters = sorted(set(letters))
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

class Solution:
    def nextGreatestLetter(self, letters, target) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        left, right = 0,len(letters)-1
        while left < right:
            # print(letters[left],letters[right])
            middle = (left + right) //2
            if target < letters[middle]:
                right = middle
            else:
                left = middle+1
        return letters[left]




s = Solution()
letters = ["c", "f", "j"]
targets = ['a','c','d','g','j','k']
for target in targets:
    print("======")
    print(target,s.nextGreatestLetter(letters,target))
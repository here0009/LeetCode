class Solution(object):
    """
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        substring = ""
        len_longest_substring = 0
        # substring = ""
        for letter in s:
            if letter not in substring:
                substring += letter
            else:
                substring_index = 0
                for substring_letter in substring:
                    if substring_letter == letter:
                        break
                    else:
                        substring_index += 1

                if substring_index == len(substring)-1:
                    substring = letter
                else:
                    substring = substring[substring_index+1:] + letter

            len_substring = len(substring)
            # print(substring)
            if  len_substring > len_longest_substring:
                len_longest_substring = len_substring

        return len_longest_substring


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ''
        res = 0
        for index,letter  in enumerate(s):
            pre_index = substring.find(letter)
            if pre_index != -1:
                res = max(res, len(substring))
                substring = substring[pre_index+1:]
            substring += letter
        res = max(res, len(substring))
        return res


s = Solution()


print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("abcdefghijklmn"))
print(s.lengthOfLongestSubstring("aab"))
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring("nfpdmpi"))

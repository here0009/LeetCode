class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longestCommonPrefix = ""
        if len(strs) == 0:
            return longestCommonPrefix
        elif len(strs) == 1:
            return strs[0]
        else:
            strs_len_list = []
            for string in strs:
                strs_len_list.append(len(string))
            min_len = min(strs_len_list)
            for index in range(min_len):
                letter = strs[0][index]
                for string in strs[1:]:
                    if string[index] != letter:
                        return longestCommonPrefix
                longestCommonPrefix += letter
        return longestCommonPrefix

s = Solution()
test = ["aa","a"]
print(s.longestCommonPrefix(test))



"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 

Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""
class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs_dict = {}
        digit_logs = []
        res = []
        for index, log in enumerate(logs):
            space = log.find(' ')
            if log[space+1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs_dict[log[space+1:]] = index
        # print(letter_logs_dict)
        # print(digit_logs)
        letter_logs_dict_keys = sorted(list(letter_logs_dict.keys()))
        # print(letter_logs_dict_keys)
        for key in letter_logs_dict_keys:
            res.append(logs[letter_logs_dict[key]])
        res.extend(digit_logs)
        return res

s = Solution()
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(s.reorderLogFiles(logs))




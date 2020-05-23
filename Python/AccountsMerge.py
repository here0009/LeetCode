"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

class Solution:
    def accountsMerge(self, accounts):
        """
        use a list of set to store the emails
        """
        res = dict()
        names = set()
        for account in accounts:
            name, emails = account[0], set(account[1:])
            # print(res)
            if name not in res:
                res[name] = [set(emails)]
            else:
                tmp = []
                for i,e in enumerate(res[name]):
                    if len(e & emails) > 0:
                        emails |= e
                    else:
                        tmp.append(e)
                tmp.append(emails)
                res[name] = tmp

        res_list = []
        for k, v in res.items():
            for e in v:
                res_list.append([k] + sorted(list(e)))
        return res_list

s = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(s.accountsMerge(accounts))
accounts = [['DLF']]
print(s.accountsMerge(accounts))

accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
print(s.accountsMerge(accounts))
output = [["David","David0@m.co","David1@m.co","David2@m.co"],["David","David2@m.co","David3@m.co","David4@m.co","David5@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"]]
expected = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
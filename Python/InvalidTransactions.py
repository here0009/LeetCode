"""
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions):
        res = set()
        name_city_dict = defaultdict(list)
        for t in transactions:
            list_t = t.split(',')
            name_city_dict[list_t[0]].append(list_t)
            if int(list_t[2]) > 1000:
                res.add(t)

        # print(name_city_dict)
        for k,v in name_city_dict.items():
            v = sorted(v,key = lambda x:int(x[1])) #time
            # print('v',v)
            for i in range(len(v)-1):
                for j in range(i+1, len(v)):
                    if int(v[j][1]) - int(v[i][1]) > 60:
                        break
                    elif int(v[j][1]) - int(v[i][1]) <= 60 and v[i][3] != v[j][3]:
                        res.add(','.join(v[i]))
                        res.add(','.join(v[j]))
                    # print('++++++++++++')
                    # print(v[i],v[j],res)
        return list(res)

s = Solution()
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
print(s.invalidTransactions(transactions))


transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
print(s.invalidTransactions(transactions))

transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
print(s.invalidTransactions(transactions))

transactions = ["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
print(s.invalidTransactions(transactions))
"""
Output:
["bob,175,221,amsterdam","bob,832,1726,barcelona","bob,820,596,bangkok","bob,689,1910,barcelona"]
Expected:
["bob,689,1910,barcelona","bob,832,1726,barcelona","bob,820,596,bangkok"]
"""
transactions = ["alex,741,1507,barcelona","xnova,683,1149,amsterdam","bob,52,1152,beijing","bob,137,1261,beijing","bob,607,14,amsterdam","bob,307,645,barcelona","bob,220,105,beijing","xnova,914,715,beijing","alex,279,632,beijing"]
print(s.invalidTransactions(transactions))

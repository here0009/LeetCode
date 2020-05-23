"""
Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

 

Example 1:

Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito". 
Example 2:

Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
Explanation: 
For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".
Example 3:

Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
 

Constraints:

1 <= orders.length <= 5 * 10^4
orders[i].length == 3
1 <= customerNamei.length, foodItemi.length <= 20
customerNamei and foodItemi consist of lowercase and uppercase English letters and the space character.
tableNumberi is a valid integer between 1 and 500.
"""
class Solution:
    def displayTable(self, orders):
        tables_set = set()
        foods_set = set()
        for name, table, food in orders:
            tables_set.add(int(table))
            foods_set.add(food)

        tables = sorted(list(tables_set))
        tables_index = dict(zip(tables, range(len(tables))))
        foods = sorted(list(foods_set))
        foods_index = dict(zip(foods, range(len(foods))))
        matrix = [[0]*len(foods) for _ in range(len(tables))]
        for name, table,food in orders:
            matrix[tables_index[int(table)]][foods_index[food]] += 1

        res = []
        header = ['Table'] + foods
        res.append(header)
        for i in range(len(tables)) :
            row = [str(tables[i])] + matrix[i]
            res.append([str(i) for i in row])
        return res

from collections import defaultdict
from collections import Counter
class Solution:
    def displayTable(self, orders):
        table_set = set()
        food_set = set()
        desk = defaultdict(Counter)
        for _, table, food in orders:
            table_set.add(table)
            food_set.add(food)
            desk[table][food] += 1
        res = []
        table_list = sorted(list(table_set), key = int)
        food_list = sorted(list(food_set))
        res.append(['Table'] + food_list)
        for t in table_list:
            res.append([t] + [str(desk[t][f]) for f in food_list])
        return res

S = Solution()
orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
# Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 

print(S.displayTable(orders))

orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
print(S.displayTable(orders))


orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(S.displayTable(orders))
# Output:
# [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["10","1","0","0","0"],["3","0","2","1","0"],["5","0","1","0","1"]]
# Expected:
# [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
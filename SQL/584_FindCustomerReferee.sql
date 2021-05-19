/*
Given a table customer holding customers information and the referee.

+------+------+-----------+
| id   | name | referee_id|
+------+------+-----------+
|    1 | Will |      NULL |
|    2 | Jane |      NULL |
|    3 | Alex |         2 |
|    4 | Bill |      NULL |
|    5 | Zack |         1 |
|    6 | Mark |         2 |
+------+------+-----------+
Write a query to return the list of customers NOT referred by the person with id '2'.

For the sample data above, the result is:

+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-customer-referee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

SELECT name
    FROM customer
    WHERE referee_id IS NULL OR referee_id != 2;
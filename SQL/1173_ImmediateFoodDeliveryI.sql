/*
Table: Delivery

+-----------------------------+---------+
| Column Name                 | Type    |
+-----------------------------+---------+
| delivery_id                 | int     |
| customer_id                 | int     |
| order_date                  | date    |
| customer_pref_delivery_date | date    |
+-----------------------------+---------+
delivery_id is the primary key of this table.
The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

If the preferred delivery date of the customer is the same as the order date then the order is called immediate otherwise it's called scheduled.

Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

The query result format is in the following example:

Delivery table:
+-------------+-------------+------------+-----------------------------+
| delivery_id | customer_id | order_date | customer_pref_delivery_date |
+-------------+-------------+------------+-----------------------------+
| 1           | 1           | 2019-08-01 | 2019-08-02                  |
| 2           | 5           | 2019-08-02 | 2019-08-02                  |
| 3           | 1           | 2019-08-11 | 2019-08-11                  |
| 4           | 3           | 2019-08-24 | 2019-08-26                  |
| 5           | 4           | 2019-08-21 | 2019-08-22                  |
| 6           | 2           | 2019-08-11 | 2019-08-13                  |
+-------------+-------------+------------+-----------------------------+

Result table:
+----------------------+
| immediate_percentage |
+----------------------+
| 33.33                |
+----------------------+
The orders with delivery id 2 and 3 are immediate while the others are scheduled.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/immediate-food-delivery-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


SELECT ROUND(t1.same_date_order/t2.total_order*100, 2) immediate_percentage
    FROM
    (SELECT count(*) same_date_order
            FROM Delivery
            WHERE order_date = customer_pref_delivery_date) t1
    JOIN
    (SELECT count(*) total_order
            FROM Delivery) t2

select round (
    (select count(*) from Delivery where order_date = customer_pref_delivery_date) / 
    (select count(*) from Delivery) * 100,
    2
) as immediate_percentage

select round (
    sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) /
    count(*) * 100,
    2
) as immediate_percentage
from Delivery


select round (
    sum(order_date = customer_pref_delivery_date) /
    count(*) * 100,
    2
) as immediate_percentage
from Delivery

-- 作者：LeetCode-Solution
-- 链接：https://leetcode-cn.com/problems/immediate-food-delivery-i/solution/ji-shi-shi-wu-pei-song-i-by-leetcode-solution/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
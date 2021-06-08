/*
Select all employee's name and bonus whose bonus is < 1000.

Table:Employee

+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId is the primary key column for this table.
Table: Bonus

+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId is the primary key column for this table.
Example ouput:

+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/employee-bonus
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
SELECT e.name, b.bonus
    FROM Employee e
    LEFT JOIN Bonus b
    ON e.empId = b.empId
    WHERE b.bonus is null OR b.bonus < 1000
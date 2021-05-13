/*
Table: Employee

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| team_id       | int     |
+---------------+---------+
employee_id is the primary key for this table.
Each row of this table contains the ID of each employee and their respective team.
Write an SQL query to find the team size of each of the employees.

Return result table in any order.

The query result format is in the following example:

Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
Result table:
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+
Employees with Id 1,2,3 are part of a team with team_id = 8.
Employees with Id 4 is part of a team with team_id = 7.
Employees with Id 5,6 are part of a team with team_id = 9.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-team-size
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

Create table If Not Exists Employee (employee_id int, team_id int)
Truncate table Employee
insert into Employee (employee_id, team_id) values ('1', '8')
insert into Employee (employee_id, team_id) values ('2', '8')
insert into Employee (employee_id, team_id) values ('3', '8')
insert into Employee (employee_id, team_id) values ('4', '7')
insert into Employee (employee_id, team_id) values ('5', '9')
insert into Employee (employee_id, team_id) values ('6', '9')




# Self Join
SELECT e1.employee_id, COUNT(*) AS team_size
FROM Employee e1 JOIN Employee e2 USING (team_id)
GROUP BY e1.employee_id
ORDER BY e1.employee_id;

SELECT
    employee_id,
    COUNT(employee_id) OVER(PARTITION BY team_id) AS team_size
FROM Employee
ORDER BY employee_id;

/*
作者：Markov015
链接：https://leetcode-cn.com/problems/find-the-team-size/solution/san-chong-fang-fa-self-join-correlated-subquerry-w/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
*/


SELECT e.employee_id, t.team_size
    FROM Employee e
    INNER JOIN(
        SELECT team_id, count(employee_id) team_size
            FROM Employee
            GROUP BY team_id
    ) AS t
    ON e.team_id = t.team_id;
/*
Table my_numbers contains many numbers in column num including duplicated ones.
Can you write a SQL query to find the biggest number, which only appears once.

+---+
|num|
+---+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 | 
For the sample data above, your query should return the following result:
+---+
|num|
+---+
| 6 |
Note:
If there is no such number, just output null.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biggest-single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


# the following one is not right because the max function is for each group, not the entire table.
SELECT MAX(num)
    FROM my_numbers
    GROUP BY num
    HAVING COUNT(*) = 1

SELECT MAX(num) AS num
    FROM
    (SELECT num
            FROM my_numbers
            GROUP BY num
            HAVING COUNT(*) = 1) AS t1


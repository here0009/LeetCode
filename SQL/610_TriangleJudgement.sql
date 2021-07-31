/*
A pupil Tim gets homework to identify whether three line segments could possibly form a triangle.
 

However, this assignment is very heavy because there are hundreds of records to calculate.
 

Could you help Tim by writing a query to judge whether these three sides can form a triangle, assuming table triangle holds the length of the three sides x, y and z.
 

| x  | y  | z  |
|----|----|----|
| 13 | 15 | 30 |
| 10 | 20 | 15 |
For the sample data above, your query should return the follow result:
| x  | y  | z  | triangle |
|----|----|----|----------|
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/triangle-judgement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


SELECT x, y, z,
    CASE WHEN x + y > z AND x + z > y AND z + y > x
    THEN 'Yes' ELSE 'No'
    END
    AS 'triangle'
FROM triangle

SELECT x, y, z,
    IF(x + y <= z OR x + z <= y OR y + z <= x, "No", "Yes") AS triangle
FROM triangle

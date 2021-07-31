/*+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some game.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.
 

Write a SQL query that reports the device that is first logged in for each player.

The query result format is in the following example:

Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+-----------+
| player_id | device_id |
+-----------+-----------+
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |
+-----------+-----------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/game-play-analysis-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

SELECT player_id, device_id
    FROM Activity
    WHERE (player_id, event_date) IN
    (
        SELECT player_id, MIN(event_date)
        FROM Activity
        GROUP BY player_id
    )

select player_id, device_id
from (select player_id, device_id, dense_rank() over(partition by player_id order by event_date asc) rk from activity) a
where a.rk=1

select player_id,device_id from (select 
player_id,
case when @player = player_id then @num := @num+1
     when @player := player_id then @num :=1
     end as num,
device_id
from Activity a, (select @player:=0,@num:=0)b order by player_id, a.event_date asc )t where t.num =1;
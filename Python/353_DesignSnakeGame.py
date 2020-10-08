"""
Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

Example:

Given width = 3, height = 2, and food = [[1,2],[0,1]].

Snake snake = new Snake(width, height, food);

Initially the snake appears at position (0,0) and the food at (1,2).

|S| | |
| | |F|

snake.move("R"); -> Returns 0

| |S| |
| | |F|

snake.move("D"); -> Returns 0

| | | |
| |S|F|

snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

| |F| |
| |S|S|

snake.move("U"); -> Returns 1

| |F|S|
| | |S|

snake.move("L"); -> Returns 2 (Snake eats the second food)

| |S|S|
| | |S|

snake.move("U"); -> Returns -1 (Game over because snake collides with border)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-snake-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import deque
class SnakeGame:
    """
    TLE, try to repalce the matrix with a set
    """
    def __init__(self, width: int, height: int, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.matrix = [[0]*width for _ in range(height)]  # 1 for snake, 2 for food
        self.food = food + [[float('inf'), float('inf')]]
        self.f_index = 0
        self.snake = deque([(0, 0)])
        self.score = 0
        self.matrix[0][0] = 1
        self.width = width
        self.height = height
        self.directions = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

    def inRange(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        fi, fj = self.food[self.f_index]
        si, sj = self.snake[0]
        di, dj = self.directions[direction]
        si, sj = si+di, sj+dj
        ti, tj = self.snake[-1]
        if not self.inRange(si,sj) or (self.matrix[si][sj] == 1 and (si,sj) != (ti,tj)):
            return -1
        if (si,sj) == (fi,fj):
            self.score += 1
            self.f_index += 1
        else:
            tmpi, tmpj = self.snake.pop()
            self.matrix[tmpi][tmpj] = 0
        self.matrix[si][sj] = 1
        self.snake.appendleft((si,sj))
        print(direction, si, sj)
        print('+++++++')
        for row in self.matrix:
            print(row)
        return self.score


from collections import deque
class SnakeGame:
    """
    the snake's body is moving together, so the head and tail won't collide, if the tail is the next position of head
    """
    def __init__(self, width: int, height: int, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.snake_set = set([(0,0)])
        self.food = food + [[float('inf'), float('inf')]]
        self.f_index = 0
        self.snake = deque([(0, 0)])
        self.score = 0
        self.width = width
        self.height = height
        self.directions = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}

    def inRange(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.width

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        fi, fj = self.food[self.f_index]
        si, sj = self.snake[0]
        di, dj = self.directions[direction]
        si, sj = si+di, sj+dj
        ti, tj = self.snake[-1]
        if not self.inRange(si,sj) or ((si,sj) in self.snake_set and (si,sj) != (ti,tj)):
            return -1
        if (si,sj) == (fi,fj):
            self.score += 1
            self.f_index += 1
        else:
            self.snake_set.remove(self.snake.pop())
        self.snake_set.add((si,sj))
        self.snake.appendleft((si,sj))
        return self.score
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

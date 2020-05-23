"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9
"""
class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        len_cells = len(cells)
        N = N%14
        if N == 0:
            N = 14
        for _i in range(N):
            new_cells = [0]
            for j in range(1,len_cells-1):
                if cells[j-1] == cells[j+1]:
                    new_cells.append(1)
                else:
                    new_cells.append(0)

            new_cells.append(0)
            cells = new_cells
            # print("Days",_i+1)
            # print(cells)
        return cells
s = Solution()
cells = [0,1,0,1,1,0,0,1]
print(s.prisonAfterNDays(cells, 7))

cells = [1,0,0,1,0,0,1,0]
N = 1000000000
print(s.prisonAfterNDays(cells, N))


cells = [1, 0, 0, 1, 0, 0, 0, 1]
N = 826
print(s.prisonAfterNDays(cells, N))

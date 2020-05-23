class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = 0
        y = 0
        z = 0
        z_len = 0 # the max length of the inner list
        for inner_list in grid:
            if len(inner_list) > z_len:
                z_len = len(inner_list)

        z_max = [0] * z_len
        for inner_list in grid:
            for index, value in enumerate(inner_list):
                if value != 0:
                    x += 1
                if value > z_max[index]:
                    z_max[index] = value
            y += max(inner_list)
        z = sum(z_max)
        return x + y + z

s = Solution()
input_list = [[2]]
print(s.projectionArea(input_list))

input_big_list =[ [[1,2],[3,4]], [[1,0],[0,2]], [[1,1,1],[1,0,1],[1,1,1]], [[2,2,2],[2,1,2],[2,2,2]] ]
for input_list in input_big_list:
    print(input_list)
    print(s.projectionArea(input_list))
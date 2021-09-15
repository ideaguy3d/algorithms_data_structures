from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]):
        count = 0
        row_len = len(grid)
        col_len = len(grid[0])
        
        def dfs(r, c):
            grid[r][c] = '0'
            if r - 1 >= 0 and grid[r - 1][c] == '1':
                dfs(r - 1, c)
            if c - 1 >= 0 and grid[r][c - 1] == '1':
                dfs(r, c - 1)

            if r + 1 < row_len and grid[r + 1][c] == '1':
                dfs(r + 1, c)
            if c + 1 < col_len and grid[r][c + 1] == '1':
                dfs(r, c + 1)

        for row in range(0, row_len):
            for col in range(0, col_len):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count

#

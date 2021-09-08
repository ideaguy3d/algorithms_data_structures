from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m_row, n_col = len(grid), len(grid[0])
        dp = [[[0, 0]] * (n_col + 2) for _ in range(m_row + 2)]
        ans = []

        for i in range(1, m_row + 1):
            for j in range(1, n_col + 1):
                ans.append(grid[i - 1][j - 1])
                dp[i][j] = [grid[i - 1][j - 1], grid[i - 1][j - 1]]
                dp[i][j][0] += dp[i - 1][j - 1][0]
                dp[i][j][1] += dp[i - 1][j + 1][1]
                # INNER_INNER_LOOP
                for win in range(1, min(m_row, n_col)):
                    x1, y1 = i - win, j - win
                    x2, y2 = i - win, j + win
                    x3, y3 = i - win - win, j
                    if not (all(1 <= x < m_row + 1 for x in [x1, x2, x3])
                            and all(1 <= y < n_col + 1 for y in [y1, y2, y3])):
                        break
                    bottom_to_left = dp[i][j][0] - dp[x1 - 1][y1 - 1][0]
                    bottom_to_right = dp[i][j][1] - dp[x2 - 1][y2 + 1][1]
                    left_to_top = dp[x1][y1][1] - dp[x3 - 1][y3 + 1][1]
                    right_to_top = dp[x2][y2][0] - dp[x3 - 1][y3 - 1][0]
                    vert_sum = grid[i - 1][j - 1] + grid[x1 - 1][y1 - 1] + grid[x2 - 1][y2 - 1] + grid[x3 - 1][y3 - 1]
                    cur = bottom_to_left + bottom_to_right + left_to_top + right_to_top - vert_sum
                    ans.append(cur)
        return sorted(set(ans), reverse=True)[:3]


class Solution2:
    def getBiggestThree(self):
        pass


inputs = [
    [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[7, 7, 7]]
]
s = Solution()
s.getBiggestThree(inputs[1])

#

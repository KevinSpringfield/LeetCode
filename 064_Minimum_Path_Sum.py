'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

example:

grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

represents
1 3 1
1 5 1
4 2 1

Answer is 1 + 3 + 1 + 1 + 1 = 7

'''

class Solution:
    def create_dp(self, m, n):
        return [[0 for _ in range(n)] for _ in range(m)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]

        dp = self.create_dp(m, n)

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]

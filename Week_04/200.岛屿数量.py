#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        if not grid:
            return count
        row,column = len(grid),len(grid[0]) 
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    count += 1
                    self.helper(grid,i,j)
        return count
    
    def helper(self,grid,i,j):
        row,column = len(grid),len(grid[0])
        grid[i][j] = '0'
        for x,y in {(0,1),(0,-1),(1,0),(-1,0)}:
            new_i,new_j = i+x,j+y
            if 0 <=new_i< row and 0 <=new_j< column and grid[new_i][new_j] == '1':
                self.helper(grid,new_i,new_j)
# @lc code=end


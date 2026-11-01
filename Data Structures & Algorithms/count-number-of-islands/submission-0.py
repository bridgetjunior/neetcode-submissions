class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        count = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)] # horizontally or vertically

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    count+=1 #island found

                    stack = [(r,c)]
                    grid[r][c] = '0' #sinking the island

                    while stack:
                        curr_r, curr_c = stack.pop()
                        for dr, dc in directions:
                            nr = dr + curr_r
                            nc = dc + curr_c

                            if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == '1':
                                grid[nr][nc] = '0' 
                                stack.append((nr, nc)) 

        return count
                            






        
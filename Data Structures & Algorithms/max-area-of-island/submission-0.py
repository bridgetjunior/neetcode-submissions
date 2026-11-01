class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, columns = len(grid), len(grid[0])

        max_area = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    current_area = 1

                    stack = [(r,c)]
                    grid[r][c] = 0 

                    while stack:
                        curr_r, curr_c = stack.pop()

                        for dr, dc in directions:
                            nr = dr + curr_r
                            nc = dc + curr_c

                            if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                                grid[nr][nc] = 0
                                current_area +=1
                                stack.append((nr,nc))
                    max_area = max(current_area, max_area)

        return max_area


                    


        
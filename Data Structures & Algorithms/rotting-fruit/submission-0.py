class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        fresh = 0
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh+= 1
                if grid[r][c] == 2:
                    queue.append((r,c,0))


        if fresh == 0:
            return 0

        while queue:
            curr_r, curr_c, minute = queue.popleft()

            for dr, dc in directions:
                nr = dr + curr_r
                nc = dc + curr_c

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                    fresh-= 1
                    grid[nr][nc] = 2
                    queue.append((nr,nc,minute + 1 ))

        
        return minute if fresh == 0 else -1 


        

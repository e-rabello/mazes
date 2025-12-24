import pygame, random, sys

# Increase recursion limit so it doesn't crash on bigger mazes
sys.setrecursionlimit(2000)

# Config
TILE = 20
SIZE = 20 
GW = (SIZE * 2) + 1
WIDTH = HEIGHT = GW * TILE

# Colors
C_BG = (20, 20, 20)
C_WALL = (100, 100, 100)
C_PATH = (200, 200, 200)
C_BOT = (255, 50, 50)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
grid = []

for i in range(GW):
    row = [] 
    for j in range(GW):
        row.append(0)
    grid.append(row)

def draw():
    win.fill(C_BG)
    
    for y in range(GW):
        for x in range(GW):
            if grid[y][x]:
                pygame.draw.rect(win, C_PATH, (x * TILE, y * TILE, TILE, TILE))
    pygame.display.flip()

def carve(x, y):
    grid[y][x] = 1
    
    # Quick visual update
    draw()
    pygame.draw.rect(win, C_BOT, (x * TILE, y * TILE, TILE, TILE))
    pygame.display.flip()
    pygame.time.delay(10)

    dirs = [(0, 2), (0, -2), (2, 0), (-2, 0)] # Up, Down, Left, Right
    random.shuffle(dirs)

    for dx, dy in dirs:
        nx = x + dx
        ny =  y + dy
        
        if 0 < nx < (GW - 1) and 0 < ny < (GW - 1) and grid[ny][nx] == 0:
            
            # Carve the wall
            wall_x = x + (dx // 2)
            wall_y = y + (dy // 2)
            grid[wall_y][wall_x] = 1

            carve(nx, ny)

def clean_maze(maze):
    
    for i in range(GW):
        for j in range(GW):
            maze[i][j] = 0
    return


def main():

    carve(1, 1)
    
    while True:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Press 'r' to generate a new maze
            if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
                clean_maze(grid)
                carve(1, 1)

if __name__ == "__main__":
    main()

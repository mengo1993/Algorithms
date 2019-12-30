import pygame
import random
import sys

FPS = 100
SQUARE_L = 5
N_SQUARES_W, N_SQUARES_H = 200, 120
N_OBSTACLES = 10000
OBSTACLES_RGB = (10, 10, 10)
ESCAPER_RGB = (10, 10, 255)
EXIT_RGB = (10, 255, 10)
BACK_RGB = (255, 255, 255)

pygame.init()
fpsClock = pygame.time.Clock()
width, height = SQUARE_L * N_SQUARES_W, SQUARE_L * N_SQUARES_H
screen = pygame.display.set_mode((width, height))

map_infos = [ [ 0 for _ in range(N_SQUARES_W) ] for _ in range(N_SQUARES_H) ]
for obstacle in range(N_OBSTACLES):
    row = random.randint(0, N_SQUARES_H - 1)
    col = random.randint(0, N_SQUARES_W - 1)
    map_infos[row][col] = "OBSTACLE"

escaper_row, escaper_col = 0,0
map_infos[escaper_row][escaper_col] = "ESCAPER"

exit_row, exit_col = N_SQUARES_H - 1, N_SQUARES_W - 1
map_infos[exit_row][exit_col] = "EXIT"

def exit_finder():
    row_queue, col_queue = [], []
    visited = [ [ False for _ in range(N_SQUARES_W) ] for _ in range(N_SQUARES_H) ]
    parents = [ [ None for _ in range(N_SQUARES_W) ] for _ in range(N_SQUARES_H) ]
    visited[escaper_row][escaper_col] = True
    row_queue.append(escaper_row)
    col_queue.append(escaper_col)
    exit_reached = False

    def reconstructPath():
        current = (exit_row, exit_col)
        path = [current]
        while current != None:
            curr_r, curr_col = current[0], current[1]
            current = parents[curr_r][curr_col]
            if current != None: path.append(current)
        path.reverse()
        return path

    def explore_nbrs(r, c):

        rr = [0, 0, 1, -1]
        cc = [1, -1, 0, 0]

        for indx in range(4):
            nbr_r, nbr_c = r + rr[indx], c + cc[indx]
            if nbr_r > N_SQUARES_H - 1 or nbr_r < 0 or nbr_c > N_SQUARES_W - 1 or nbr_c < 0: continue
            if map_infos[nbr_r][nbr_c] == "OBSTACLE" or visited[nbr_r][nbr_c]: continue

            if map_infos[nbr_r][nbr_c] == "EXIT":
                parents[nbr_r][nbr_c] = (r,c)
                return True
            else:
                visited[nbr_r][nbr_c] = True
                row_queue.append(nbr_r)
                col_queue.append(nbr_c)
                parents[nbr_r][nbr_c] = (r,c)

    while len(row_queue) > 0:
        r = row_queue.pop(0)
        c = col_queue.pop(0)

        exit_reached = explore_nbrs(r,c)
        if exit_reached: break

    if exit_reached:
        path = reconstructPath()
        return path
    else:
        return [] # not possible to reach the end


exit_path = exit_finder()
path_index = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

    # Update.
    try: escaper_row, escaper_col = exit_path[path_index]
    except IndexError: print "Impossible to reach the end"
    if path_index < len(exit_path) - 1: path_index += 1
    map_infos[escaper_row][escaper_col] = "ESCAPER"

    # Draw.
    screen.fill((BACK_RGB))
    for row_index, row, in enumerate(map_infos):
        for col_index, col in enumerate(row):
            if col == "OBSTACLE":
                pygame.draw.rect(screen, OBSTACLES_RGB, (col_index * SQUARE_L, row_index * SQUARE_L,SQUARE_L, SQUARE_L))
            elif col == "ESCAPER":
                pygame.draw.rect(screen, ESCAPER_RGB, (col_index * SQUARE_L, row_index * SQUARE_L,SQUARE_L, SQUARE_L))
            elif col == "EXIT":
                pygame.draw.rect(screen, EXIT_RGB, (col_index * SQUARE_L, row_index * SQUARE_L,SQUARE_L, SQUARE_L))

    pygame.display.flip()
    fpsClock.tick(FPS)








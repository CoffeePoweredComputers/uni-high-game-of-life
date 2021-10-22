import pygame
import numpy as np
import sys

#
# Setup the colors
#
COLOR_ABOUT_TO_DIE = (155, 155, 155)
COLOR_ALIVE = (255, 255, 255)
COLOR_BACKGROUND = (0, 0, 0)
COLOR_GRID = (30, 30, 60)

def parse_data(fp):
    """
    Parse the glider patterns from the project directory into a list 
    of lists where each sublist is a list of integers that are either
    1 (alive cell) or 0 (dead cell).

    Arguments:
        fp (string) -> The path to the glider pattern that the user type
                       in from sys.argv[1]
    """

    with open(fp) as fin:
        data = [ list(map(int, x.split(","))) for x in fin.readlines()]
    return data


def sum_across_rows(grid):

    total = 0
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            total += grid[y, x]
    return total


def update(surface, cur, sz):
    nxt = np.zeros((cur.shape[0], cur.shape[1]))

    for r in range(cur.shape[0]):
        for c in range(cur.shape[1]):
    
            num_alive = sum_across_rows(cur[r-1:r+2, c-1:c+2]) - cur[r, c]

            if cur[r, c] == 1 and num_alive < 2 or num_alive > 3:
                color = COLOR_ABOUT_TO_DIE
            elif (cur[r, c] == 1 and 2 <= num_alive <= 3) or (cur[r, c] == 0 and num_alive == 3):
                nxt[r, c] = 1
                color = COLOR_ALIVE

            color = color if cur[r, c] == 1 else COLOR_BACKGROUND
            pygame.draw.rect(surface, color, (c*sz, r*sz, sz-1, sz-1))

    return nxt

def init(x_dim, y_dim):
    """
    This function initializes all the cells to 0 then includes the glider 
    pattern the user inputted. If the user did not input a valid pattern 
    then it defaults to a randomized starting pattern.
    """

    cells = np.zeros((y_dim, x_dim))
    pattern = np.array(parse_data(sys.argv[1]));
    pos = (10,14)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main(x_dim, y_dim, cellsize):
    pygame.init()
    surface = pygame.display.set_mode((x_dim * cellsize, y_dim * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(x_dim, y_dim)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(COLOR_GRID)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    main(120, 90, 8)

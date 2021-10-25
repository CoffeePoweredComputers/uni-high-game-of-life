import pygame
import numpy as np
import sys

#
# Setup the colors
#
COLOR_ABOUT_TO_DIE = (232, 74, 50)
COLOR_ALIVE = (232, 74, 39)
COLOR_BACKGROUND = (19, 41, 75)
COLOR_GRID = (30, 30, 60)

def parse_data(fp):
    """
    Parse the glider patterns from the project directory into a list of lists
    where each sublist is a list of integers that are either 1 (alive cell) or
    0 (dead cell).

    Arguments:
        fp (string) -> The path to the glider pattern that the user type
                       in from sys.argv[1]
    """
    pass


def sum_across_rows(grid):
    """
    Takes a 2d numpy array and returnsthe sum of value across all subarrays.

    Arguments:
        grid (np.array) -> The 2d array.
    """
    pass


def copy_pattern(grid, pattern, y_padding, x_padding):
    """
    Takes a pattern and copies that pattern onto the grid
    with some amount of padding.
    """


    #Step 1: Check if the pattern + padding will fit on the grid

    #Step 2: Iterate over the pattern and copy it onto the grid

    pass

def update(surface, curr_grid, cell_size):

    # We start off with a new grid which is what we will be updating
    new_grid = np.zeros((cur.shape[0], cur.shape[1]))

    for y in range(curr_grid.shape[0]):
        for x in range(curr_grid.shape[1]):

            # Implement the game of life using the rules
    
            pygame.draw.rect(surface, color, (x*cell_size, y*cell_size, cell_size-1, -1))

    return new_grid

def init(x_dim, y_dim):
    """
    This function initializes all the cells to 0 then includes the glider 
    pattern the user inputted. If the user did not input a valid pattern 
    then it defaults to a randomized starting pattern.
    """

    #Step 1) 
    grid = #create a numpy grid of zeroes of with the dimensions inthe parameters
    pattern = #parse the pattern given by the user via sys.argv

    # Step 2) Validate and read in the padding arguments if the user passes them in
    # otherwise default to zero 

    # Step 3) Copy the pattern onto the grid

    # Step 4) Return the result

    pass

def main(x_dim, y_dim, cellsize):
    """
    This just gets the game going. No need to modify anything here.
    """
    pygame.init()
    surface = pygame.display.set_mode((x_dim * cellsize, y_dim * cellsize))
    pygame.display.set_caption("John Conway's Game of Life")

    cells = init(x_dim, y_dim)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit("Life has finished...")

        surface.fill(COLOR_GRID)
        cells = update(surface, cells, cellsize)
        pygame.display.update()

if __name__ == "__main__":
    main(90, 90, 10)

#! /usr/bin/env python3.7

"""Model an island habitat."""


class Island:
    """Model an island.

    An n X n grid where a zero value indicates an unoccupied cell.
    """

    def __init__(self, n, prey_cnt=0, predator_cnt=0):
        """Initialize cell to all 0's, then fill with animals"""
        self.__grid_size = n
        self.__grid = []
        for _ in range(n):
            row = [0] * n  # row is a list of n zeros
            self.__grid.append(row)
        # self._init_animals(prey_cnt, predator_cnt)

    @property
    def grid_size(self):
        """Get the island size."""
        return self.__grid_size

    @property
    def grid(self):
        """Get the grid representing the island."""
        return self.__grid

    def __str__(self):
        """String representation for printing.

        (0,0) will be in the lower-left corner.
        """
        spaces = ""
        for j in range(self.grid_size - 1, -1, -1):  # print row size-1 first
            for i in range(self.grid_size):  # each row starts at 0
                if not self.grid[i][j]:
                    # print a '.' for an empty space
                    spaces += "{:<2s}".format("." + "  ")
                else:
                    spaces += "{:<2s}".format((str(self.grid[i][j])) + "  ")
            spaces += "\n"
        return spaces

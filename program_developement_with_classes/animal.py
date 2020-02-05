#! /usr/bin/env python3.7
"""Animal classes for use in the simulation."""


class Animal(object):
    """Base class for predator/prey animals in the simulation."""

    def __init__(self, island, name="", x=0, y=0):
        """Initialize the animals and their positions."""
        self.__island = island
        self.__name = name
        self.__x = x
        self.__y = y

    @property
    def island(self):
        """Get the Island the Animal is on."""
        return self.__island

    @property
    def name(self):
        """Get the Animal's name."""
        return self.__name

    @property
    def position(self):
        """Get the Animal's position (its x, y coordinates) on the Island."""
        return (self.__x, self.__y)

    def __str__(self):
        """Print a string representation of the animal."""
        return self.name

"""2D Point class."""

from math import sqrt


class Point:
    """A 2D point."""

    def __init__(self, x=0.0, y=0.0):
        """
        Initialize an instance of Point.

        Keyword Arguments:
            x {float} -- The x-coordinate of the point (default: {0})
            y {float} -- The y-coordinate of the point (default: {0})
        """
        self._x = x
        self._y = y

    def add(self, other):
        """
        Compute the vector sum of two points.

        Arguments:
            other {Point} -- The Point to be added to self.

        Returns:
            Point -- A new Point object representing the vector sum of
            the original two points.

        """
        return Point(self._x + other._x, self._y + other._y)

    def euclidian_distance(self, other):
        """
        Compute the euclidian distance between two points.

        Arguments:
            other {Point} -- The Point to which the distance is to be
            calculated.

        Returns:
            float -- The distance between the two points.

        """
        return sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)

    def manhattan_distance(self, other):
        """Compute the Manhattan distance between two points.

        Arguments:
            other {Point} -- The Point to which the distance is to be
            calculated.

        Returns:
            float -- The distance between the two points.

        """
        return abs(self._x - other._x) + abs(self._y - other._y)

    def __str__(self):
        """Return a human-readable representation of the Point."""
        return f"({self._x:.1f}, {self._y:.1f})"

    def __repr__(self):
        """
        Return a machine-readable representation of the Point.

        This is the canonical representation of the Point, it should be
        in a format that resembles executable Python code.
        """
        return f"point.Point({self._x:f}, {self._y:f})"

    def __add__(self, other):
        """Compute the vector sum of two points.

        Arguments:
            other {Point} -- The Point to be added to self.

        Returns:
            Point -- A new Point object representing the vector sum of
            the original two points.

        """
        return Point(self._x + other._x, self._y + other._y)

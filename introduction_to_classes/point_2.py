"""2D Point class."""

from math import sqrt


class Point:
    """A 2D point with "proper" private data and getters/setters."""

    def __init__(self, x=0.0, y=0.0):
        """
        Initialize an instance of Point.

        Keyword Arguments:
            x {float} -- The x-coordinate of the point (default: {0})
            y {float} -- The y-coordinate of the point (default: {0})
        """
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """Access the x-coordinate of the point.

        Returns:
            float -- The x-coordinate of the point.

        """
        return self.__x

    @x.setter
    def x(self, new_value):
        """Set the x-coordinate.

        Valid x-coordinates must be either of type int or type float.

        Arguments:
            new_value {int or float} -- The new x-coordinate of the
            point.

        """
        if isinstance(new_value, (int, float)):
            self.__x = new_value
        else:
            pass
            # this would be a good time to raise an exception

    @property
    def y(self):
        """Access the y-coordinate of the point.

        Returns:
            float -- The y-coordinate of the point.

        """
        return self.__y

    @y.setter
    def y(self, new_value):
        """Set the y-coordinate.

        Valid y-coordinates must be either of type int or type float.

        Arguments:
            new_value {int or float} -- The new y-coordinate of the
            point.

        """
        if isinstance(new_value, (int, float)):
            self.__y = new_value
        else:
            pass
            # this would be a good time to raise an exception

    def add(self, other):
        """
        Compute the vector sum of two points.

        Arguments:
            other {Point} -- The Point to be added to self.

        Returns:
            Point -- A new Point object representing the vector sum of
            the original two points.

        """
        return Point(self.x + other.x, self.y + other.y)

    def euclidian_distance(self, other):
        """
        Compute the euclidian distance between two points.

        Arguments:
            other {Point} -- The Point to which the distance is to be
            calculated.

        Returns:
            float -- The distance between the two points.

        """
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def manhattan_distance(self, other):
        """Compute the Manhattan distance between two points.

        Arguments:
            other {Point} -- The Point to which the distance is to be
            calculated.

        Returns:
            float -- The distance between the two points.

        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __str__(self):
        """Return a human-readable representation of the Point."""
        return f"({self.x:.1f}, {self.y:.1f})"

    def __repr__(self):
        """
        Return a machine-readable representation of the Point.

        This is the canonical representation of the Point, it should be
        in a format that resembles executable Python code.
        """
        return f"point.Point({self.x:f}, {self.y:f})"

    def __add__(self, other):
        """Compute the vector sum of two points.

        Arguments:
            other {Point} -- The Point to be added to self.

        Returns:
            Point -- A new Point object representing the vector sum of
            the original two points.

        """
        return Point(self.x + other.x, self.y + other.y)

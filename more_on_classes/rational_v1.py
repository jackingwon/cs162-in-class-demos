#! /usr/bin/env python3.7

"""A class representing rational numbers.

A rational number is a number that can be expressed as the ratio of two
integer values. That is,

    A rational number is a number that can be in the form p/q
    where p and q are integers and q is not equal to zero.
"""


# pylint: disable=invalid-name


class Rational:
    """Rational with numerator and denominator. Denominator parameter defaults to 1."""

    def __init__(self, numerator, denominator=1):
        """Initialize an instance of Rational."""
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        """Get the value of the numerator."""
        return self.__numerator

    @property
    def denominator(self):
        """Get the value of the denominator."""
        return self.__denominator

    # Note there is no accompanying setter for either numerator or denominator.

    def __str__(self):
        """Compute string representation for printing."""
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        """Use in the interpreter. Call __str__ for now."""
        return self.__str__()


if __name__ == "__main__":
    rational_1 = Rational(1, 2)
    print(rational_1)
    print(f"numerator = {rational_1.numerator}")
    print(f"denominator = {rational_1.denominator}")
    print(type(rational_1))
    print(isinstance(rational_1, Rational))
    print(isinstance(rational_1, int))

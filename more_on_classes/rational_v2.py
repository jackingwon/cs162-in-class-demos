#! /usr/bin/env python3.7

"""A class representing rational numbers.
A rational number is a number that can be expressed as the ratio of two
integer values. That is,

    A rational number is a number that can be in the form p/q
    where p and q are integers and q is not equal to zero.
"""


# pylint: disable=invalid-name


def gcd(bigger, smaller):
    """Calculate the greatest common divisor of two positive integers."""
    if not bigger > smaller:  # swap if necessary so bigger > smaller
        bigger, smaller = smaller, bigger

    while smaller != 0:
        remainder = bigger % smaller
        bigger, smaller = smaller, remainder

    return bigger


def lcm(a, b):
    """Calculate the lowest common multiple of two positive integers."""
    return (a * b) // gcd(a, b)


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

    def __str__(self):
        """Compute string representation for printing."""
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        """Use in the interpreter. Call __str__ for now."""
        return self.__str__()

    def __add__(self, other):
        """Add two Rationals."""
        # find a common denominator (lcm)
        lcm_ = lcm(self.denominator, other.denominator)
        # multiply each by the lcm, then add
        numerator_sum = (lcm_ * self.numerator / self.denominator) + (
            lcm_ * other.numerator / other.denominator
        )
        return Rational(int(numerator_sum), lcm_)

    def __sub__(self, other):
        """Subtract two Rationals."""
        # subtraction is the same but with '-' instead of '+'
        lcm_ = lcm(self.denominator, other.denominator)
        numerator_diff = (lcm_ * self.numerator / self.denominator) - (
            lcm_ * other.numerator / other.denominator
        )
        return Rational(int(numerator_diff), lcm_)


if __name__ == "__main__":
    a = Rational(1, 5)
    b = Rational(2, 5)
    print(f"{a} + {b} = {a + b}")

    c = Rational(1, 5)
    d = Rational(1, 3)
    print(f"{c} + {d} = {c + d}")

    c = Rational(1, 5)
    d = Rational(1, 3)
    print(f"{c} - {d} = {c - d}")

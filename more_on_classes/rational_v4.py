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
        if isinstance(other, int):
            other = Rational(other)

        if isinstance(other, Rational):
            # find a common denominator (lcm)
            lcm_ = lcm(self.denominator, other.denominator)
            # multiply each by the lcm, then add
            numerator_sum = (lcm_ * self.numerator / self.denominator) + (
                lcm_ * other.numerator / other.denominator
            )
        else:
            pass
            # will most likely result in an exception being thrown
        return Rational(int(numerator_sum), lcm_)

    def __sub__(self, other):
        """Subtract two Rationals."""
        if isinstance(other, int):
            other = Rational(other)

        if isinstance(other, Rational):
            # subtraction is the same but with '-' instead of '+'
            lcm_ = lcm(self.denominator, other.denominator)
            numerator_diff = (lcm_ * self.numerator / self.denominator) - (
                lcm_ * other.numerator / other.denominator
            )
        else:
            pass
            # will most likely result in an exception being thrown
        return Rational(int(numerator_diff), lcm_)

    def reduce_rational(self):
        """Return the reduced fractional value as a Rational."""
        gdc_ = gcd(self.numerator, self.denominator)
        return Rational(self.numerator // gdc_, self.denominator // gdc_)

    def __eq__(self, other):
        """Compare two Rationals for equality, return Boolean."""
        if isinstance(other, int):
            other = Rational(other)

        if isinstance(other, Rational):
            # reduce both; then check that numerators and denominators are equal
            reduced_self = self.reduce_rational()
            reduced_other = other.reduce_rational()
            return (
                reduced_self.numerator == reduced_other.numerator
                and reduced_self.denominator == reduced_other.denominator
            )
        else:
            pass
            # will most likely result in an exception being thrown


if __name__ == "__main__":
    a = Rational(1, 5)
    b = Rational(3, 5)
    print(f"{a} + {b} = {a + b}")

    c = Rational(1, 5)
    d = 1
    print(f"{c} + {d} = {c + d}")

    e = Rational(3, 3)
    f = 1
    print(f"{e} == {f} is {e == f}")

    g = 1
    h = Rational(3, 3)
    print(f"{g} == {h} is {g == h}")

    c = 1
    d = Rational(1, 5)
    print(f"{c} + {d} = {c + d}")

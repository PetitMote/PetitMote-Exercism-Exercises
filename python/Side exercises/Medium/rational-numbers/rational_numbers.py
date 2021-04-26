from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        gcd_rational = gcd(numer, denom)
        numer = numer // gcd_rational
        denom = denom // gcd_rational

        if numer < 0 and denom < 0:
            numer, denom = -numer, -denom
        elif numer > 0 and denom < 0:
            numer, denom = -numer, -denom

        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = (self.numer * other.denom) - (other.numer * self.denom)
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise Exception("Division by O")
        else:
            numer = self.numer * other.denom
            denom = self.denom * other.numer
            return Rational(numer, denom)

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self

    def __pow__(self, power):
        numer = self.numer ** power
        denom = self.denom ** power
        return Rational(numer, denom)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)


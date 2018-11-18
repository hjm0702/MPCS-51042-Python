import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.gcd = math.gcd(numerator, denominator)
        self.numerator = int(numerator/self.gcd)
        self.denominator = int(denominator/self.gcd)

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise ValueError("Numerator should be an integer.")
        else:
            self._numerator= numerator

    @denominator.setter
    def denominator(self, denominator):
        if not isinstance(denominator, int):
            raise ValueError("Denominator should be an integer.")
        elif denominator == 0:
            raise ZeroDivisionError("Denominator should not be zero")
        else:
            self._denominator = denominator

    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator*other.denominator+self.denominator*other.numerator, self.denominator*other.denominator)
        elif isinstance(other, int):
            return Fraction((self.numerator+other*self.denominator), self.denominator)

    def __radd__(self, other):
        return self+other

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator*other.denominator-self.denominator*other.numerator, self.denominator*other.denominator)
        elif isinstance(other, int):
            return Fraction((self.numerator-other*self.denominator), self.denominator)

    def __rsub__(self, other):
        return self-other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator*other, self.denominator)

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)
        elif isinstance(other, int):
            return Fraction(self.numerator, self.denominator*other)

    def __rtruediv__(self, other):
        return self/other

    def __neg__(self):
        return Fraction((-1)*self.numerator, self.denominator)

if __name__ == "__main__":
    a = Fraction(0, 10)
    print(a.gcd)
    print(a)
    b = Fraction(2,1)
    c = Fraction(4,5)
    d = -3
    print(a/b)
    print(c/a)
    print(a/d)
    print(d/a)
    print (-a)

""" 一个较好的有理数类实现 """
# Module rational defines a class (a type) Rational, for rational numbers.
# More operations (methods) can be added.


class Rational:
    @staticmethod
    def _gcd(m, n):
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, num, den=1):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign
        g = Rational._gcd(num, den)
        # call function gcd defined in this class.
        self._num = sign * (num//g)
        self._den = den//g

    def num(self):
        return self._num

    def den(self):
        return self._den

    def __add__(self, another):     # mimic + operator
        den = self._den * another.den()
        num = (self._num * another.den() +
               self._den * another.num())
        return Rational(num, den)

    def __mul__(self, another):      # mimic * operator
        return Rational(self._num * another.num(),
                        self._den * another.den())

    def __floordiv__(self, another):  # mimic // operator
        if another.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * another.den(),
                        self._den * another.num())

    # ... ...
    # Other operators can be defined similarly:
    # -:__sub__, /:__truediv__, %:__mod__, etc.

    def __eq__(self, another):
        return self._num * another.den() == self._den * another.num()

    def __lt__(self, another):
        return self._num * another.den() < self._den * another.num()

    # Other comparison operators can be defined similarly:
    # !=:__ne__, <=:__le__, >:__gt__, >=:__ge__

    def __str__(self):
        return str(self._num) + "/" + str(self._den)

    def print(self):
        print(self._num, "/", self._den)


if __name__ == '__main__':
    x = Rational(3, 8)
    x = x + Rational(7, 6)
    x.print()

#    Rational(17, 0)

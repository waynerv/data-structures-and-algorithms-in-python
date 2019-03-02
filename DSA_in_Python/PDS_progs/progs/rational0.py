# Module rational defines a primitive Rational class (a type).
# More operations (methods) can be defined.


class Rational0:
    def __init__(self, num, den=1):
        self.num = num
        self.den = den

    def plus(self, another):
        den = self.den * another.den
        num = (self.num * another.den +
               self.den * another.num)
        return Rational0(num, den)

    def print(self):
        print(str(self.num)+"/"+str(self.den))


if __name__ == '__main__':
    r1 = Rational0(3,5)
    r2 = r1.plus(Rational0(7,15))
    r2.print()

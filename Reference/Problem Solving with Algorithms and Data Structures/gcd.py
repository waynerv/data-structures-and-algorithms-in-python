def gcd(m,n):
    # m & n are int.
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction():
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+'/'+str(self.den)

    def show(self):
        print(self.num, '/', self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
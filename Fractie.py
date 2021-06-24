def cmmdc(x, y):
    while y:
        r = x % y
        x = y
        y = r
    return x


class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def get_numitor(self):
        return self.numitor

    def get_numarator(self):
        return self.numarator

    def __str__(self):
        return f"{self.get_numarator()}/{self.get_numitor()}"

    def __add__(self, other):
        new_numarator = self.get_numarator()*other.get_numitor() + other.get_numarator()*self.get_numitor()
        new_numitor = self.get_numitor() * other.get_numitor()
        r = cmmdc(new_numarator, new_numitor)
        return Fractie(new_numarator//r, new_numitor//r)

    def __sub__(self, other):
        new_numarator = self.get_numarator()*other.get_numitor() - other.get_numarator()*self.get_numitor()
        new_numitor = self.get_numitor() * other.get_numitor()
        r = cmmdc(new_numarator, new_numitor)
        return Fractie(new_numarator//r, new_numitor//r)

    def inverse(self):
        return Fractie(self.get_numitor(), self.get_numarator())


f1 = Fractie(2, 3)
print(f1.get_numarator())
print(f1.get_numitor())
print(f1.inverse())

f2 = Fractie(1, 2)
print(f1 + f2)

print(f1 - f2)

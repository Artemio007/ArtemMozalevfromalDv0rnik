

class Complex:
    def __init__(self, real, imaginary):
        self. real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary <= 0:
            return f"{round(self.real, 2)}{round(self.imaginary, 2)}j"
        elif self.imaginary > 0:
            return f"{round(self.real, 2)}+{round(self.imaginary, 2)}j"

    def sum(self, reals, imaginary_s):
        self.real += reals
        self.imaginary += imaginary_s

    def sub(self, reals, imaginary_s):
        self.real -= reals
        self.imaginary -= imaginary_s

    def mul(self, reals, imaginary_s):
        self.real = self.real * reals - self.imaginary * imaginary_s
        self.imaginary = self.imaginary * reals + self.real * imaginary_s

    def div(self, reals, imaginary_s):
        self.real = (self.real * reals + self.imaginary * imaginary_s) / ((reals **2) + (imaginary_s ** 2))
        self.imaginary = (self.real * imaginary_s - self.imaginary * reals) / ((reals **2) + (imaginary_s ** 2))

    def eq(self, reals, imaginary_s):
        if imaginary_s >= 0:
            print(f"You wrote {reals}+{imaginary_s}j")
        if imaginary_s < 0:
            print(f"For eq: you wrote {reals}{imaginary_s}j")

        if self.real == reals and self.imaginary == imaginary_s:
            print(True)
        if self.real != reals and self.imaginary != imaginary_s:
            print(False)

    def abs(self):
        return (self.real ** 2) + (self.imaginary ** 2)


a = Complex(5, 12)
a.sum(-5, -6)
print(a)
a.sub(6, 2)
print(a)
a.mul(-1, 9)
print(a)
a.div(3, 7)
print(a)
a.eq(5, -12)
print(a)
print(a.abs())




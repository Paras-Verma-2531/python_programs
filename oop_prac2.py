class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square of a {self.n}  is {self.n**2} ")

    def cube(self):
        print(f"the cube  of a {self.n}  is {self.n**3} ")

    def squareroot(self):

        print(f"the square root  of a {self.n}  is {self.n**0.5} ")


num = calculator(4)
num.square()
num.cube()
num.squareroot()

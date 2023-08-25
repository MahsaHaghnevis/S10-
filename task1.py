#
##
### fractions oop
##  
#

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, other):
        result_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other):
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other):
        result_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        return Fraction(result_numerator, result_denominator)

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

a=float(input("enter the head of first fraction = "))
b=float(input("enter the down of first fraction = "))
print(f"so the first fraction is {a}/{b} ")
c=float(input("enter the head of second fraction= "))
d=float(input("enter the down of second fraction= "))
print(f"so the second fraction is {c}/{d}")

# Example usage
fraction1 = Fraction(a, b)
fraction2 = Fraction(c, d)
option=int(input("enter the option u wanna do with ur fractions \t 1-add 2-multiply 3-subtract 4-divide "))

if option==1:
    addition_result = fraction1.add(fraction2)
    print(f"Addition: {addition_result}")
elif option==2:
    print(f"({a}/{b})+({c}/{d}) = ")
    multiplication_result = fraction1.multiply(fraction2)
    print(f"Multiplication: {multiplication_result}")
elif option==3:
    subtraction_result = fraction1.subtract(fraction2)
    print(f"Subtraction: {subtraction_result}")
elif option==4:
    division_result = fraction1.divide(fraction2)
    print(f"Division: {division_result}")
else:
    print("wrong input!")
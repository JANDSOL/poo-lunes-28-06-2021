class Operation:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def sum(self):
        return self.number1 + self.number2

    def subtraction(self):
        return self.number1 - self.number2

    def multiplication(self):
        return self.number1 * self.number2

    def integer_division(self):
        if self.number2 != 0: return self.number1 / self.number2
        return 0

    def integer_division(self):
        if self.number2 != 0: return self.number1 // self.number2
        return 0

    def residue(self):
        return self.number1 % self.number2

    def exponent(self):
        return self.number1 ** self.number2
    
    def show(self):
        print('Operando1={}. Operando2={}'.format(self.number1, self. number2))


if __name__ == '__main__':
    pass

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

    def division(self):
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
        print('Operando1={}. Operando2={}'.format(self.number1,\
                                                  self. number2))


if __name__ == '__main__':
    print('Menú Operaciones Matemáticas')
    print('1) Suma\n2) Resta\n3) Multiplicación\n4) División\
           \n5) Division Entera\n6) Residuo\n7) Exponente\n8) Salir')
    option = '0'

    while option != '8':
        option = input('Elija una opción[1...8]: ')
        if option in '1234567':
            num1 = int(input('Ingrese el número 1: '))
            num2 = int(input('Ingrese el número 2: '))
        if option == '1':
            operation = Operation(num1, num2)
            print('Suma:', operation.sum())
        elif option == '2':
            operation = Operation(num1, num2)
            print('Resta:', operation.subtraction())
        elif option == '3':
            operation = Operation(num1, num2)
            print('Multiplicación:', operation.multiplication())
        elif option == '4':
            operation = Operation(num1, num2)
            print('División:', operation.division())
        elif option == '5':
            operation = Operation(num1, num2)
            print('Division Entera:', operation.integer_division())
        elif option == '6':
            operation = Operation(num1, num2)
            print('Residuo:', operation.residue())
        elif option == '7':
            operation = Operation(num1, num2)
            print('Exponente:', operation.exponent())
    print('Gracias por su visita!!!')

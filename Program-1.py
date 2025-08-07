class calculator:
    def __init__(self,a,b,operation):
        self.a=a
        self.b=b
        self.operation=operation
    def calculator(self):
        if self.operation =='add':
            return self.a + self.b
        elif self.operation =='subtract':
            return self.a-self.b
        elif self.operation =='multiply':
            return self.a*self.b
        elif self.operation =='divide':
            return self.a/self.b
        else:
            return "Invalid operation"

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
operation = input("Enter operation(add,subtract,multiply,divide):")
calc=calculator(a,b,operation)
print("Result:",calc.calculator())

class Calculator:
    calculation_type = "Calculation type: Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(cls.calculation_type)
        return a * b
    
if __name__ == "__main__":
    print("The sum is:", Calculator.add(5, 3))          
    print("The product is:", Calculator.multiply(5, 3))     
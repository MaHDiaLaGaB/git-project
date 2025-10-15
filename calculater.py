class Calculator:
    """Simple calculator for basic arithmetic operations"""
    
    def add(self, a, b, c):
        """Add two numbers"""
        return a + b + c
    
    def power(self, a, b):
        """Raise a to the power of b"""
        return a ** b

    def subtract(self, a, b, c):
        """Subtract b from a"""
        return a - b - c
    
    def multiply(self, a, b, c):
        """Multiply two numbers"""
        return a * b * c
    
    def divide(self, a, b, c):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b / c


# Example usage
if __name__ == "__main__":
    calc = Calculator()
    
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")

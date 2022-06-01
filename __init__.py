from operacoes import Calculator
from interface_poo import Interface


if __name__ == "__main__":
    interface = Interface()
    user_input = interface.view()
    
    calculator = Calculator()
    calculator.calculate(user_input)
    
    
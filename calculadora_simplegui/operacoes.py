from PySimpleGUI import *
from juncao import *


class Calculator:
    
    def calculate(Result):
        j = 0
        lista_caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '+', '-', '/', '*', '%', '(', ')', '.', ',']
                        
        for i in Result:
            if i in lista_caracteres:
                while j <= 1:
                    try:
                        j+=1
                        resultado = eval(Result)
                        return resultado
                    except:
                        return print('Invalido') 
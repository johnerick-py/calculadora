
class Calculator:
    
    def calculate(self, numero):
        
        lista_caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '+', '-', '/', '*', '%', '(', ')', '.', ',']
                        
        for i in numero:
            if i in lista_caracteres:
                try:
                    print(eval(numero))
                except:
                    print('Digite uma expressao valida.')
                    exit()
    
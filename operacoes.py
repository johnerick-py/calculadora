
class Calculator:
    
    def calculate(self, numero):
        j = 0
        lista_caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        '+', '-', '/', '*', '%', '(', ')', '.', ',']
                        
        for i in numero:
            if i in lista_caracteres:
                while j <= 1:
                    try:
                        j+=1
                        return print(eval(numero))
                    except:
                        print('Digite uma expressao valida.')
                        exit()
    
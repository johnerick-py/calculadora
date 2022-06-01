import PySimpleGUI as sg

from interface_poo import Interface
from operacoes import Calculator

class Application():
    def actions():
        # Importando o layout
        # layout = Application.view(self)

        layout = Interface.view()


        

        # Janela 
        window = sg.Window("Calculator", element_justification="c", resizable=True, margins=(0,0), layout=layout, return_keyboard_events=False)
        window = window

        # Lista painel
        panel = window["panel"]
        panel = panel

        # Events
        while True:
            event, values = window.read(timeout=1)    
            if event == sg.WINDOW_CLOSED:
                break
            
            elif event == "cancel":
                panel.update("")
            
            elif event == "seven":        
                panel.update(panel.get() + "7")

            elif event == "equal":
                result = panel.get()
                return result
                panel.update()

    def att_visor(self, valor):
        self.panel.update(valor)
        read = self.window.read(timeout=1)
        return read
        
        
            

    
if __name__ == "__main__":
    x = 0
    app = Application
    app.actions()

    calculator = Calculator()
    while x <= 10:
        
        user_input = app.actions()   
        valor = calculator.calculate(user_input)

        app.att_visor(valor)
        x += 1
        


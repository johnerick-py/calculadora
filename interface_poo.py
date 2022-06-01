import PySimpleGUI as sg
from operacoes import Calculator

class Interface:
    def __init__(self):
        # Layout
        sg.theme("DarkGrey3")
        self.layout = [
            [sg.Input(key="panel", size=(23,2)), sg.Button("c",key="cancel", size=(3,1))],
            [sg.Button("m+",key="memory+", size=(3,1)), sg.Button("m-",key="memory-", size=(3,1)), sg.Button("m=",key="memory=", size=(3,1)), sg.Button("x",key="multiply", size=(3,1))],
            [sg.Button("7",key="seven", size=(3,2)), sg.Button("8",key="eight", size=(3,2)), sg.Button("9",key="nine", size=(3,2)), sg.Button("÷",key="divide", size=(3,2))],
            [sg.Button("4",key="four", size=(3,2)), sg.Button("5",key="five", size=(3,2)), sg.Button("6",key="six", size=(3,2)), sg.Button("-",key="minus", size=(3,2))],
            [sg.Button("1",key="one", size=(3,2)), sg.Button("2",key="two", size=(3,2)), sg.Button("3",key="three", size=(3,2)), sg.Button("+",key="add", size=(3,2))],
            [sg.Button("0",key="zero", size=(3,2)), sg.Button(".",key="point", size=(3,2)), sg.Button("=",key="equal", size=(12,2))]
            ]
        
        # Janela
        self.window = sg.Window("Calculator", element_justification="c", resizable=True, margins=(0,0), layout=self.layout, return_keyboard_events=False)

        # Lista painel
        self.panel = self.window["panel"]

    def teste(self):
        
        
        user_input = Interface.view()
        calculator = Calculator()
        calculator.calculate(user_input)
        resultado = calculator.calculate(user_input)

        # Events
        while True:
            event, values = self.window.read(timeout=1)    
            if event == sg.WINDOW_CLOSED:
                break
            
            elif event == "cancel":
                self.window["panel"].update("")
            
            elif event == "seven":        
                self.panel.update(self.panel.get() + "7")

            elif event == "equal":
                result = self.panel.get() + resultado
                return result
    
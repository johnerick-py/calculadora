from tkinter import ANCHOR
from PySimpleGUI import *
from interface_po import Interface
from operacoes import Calculator
from time import sleep


class Unindo:
    
    def pegando_interface():
        
        layout = Interface.imagem_calculadora()
        
        # Set PySimpleGUI
        form = FlexForm('CALCULATOR', default_button_element_size=(5, 2),
                        auto_size_buttons=False, grab_anywhere=False, return_keyboard_events=False)
        form.Layout(layout)
        
        # Result Value
        Result = ''
        
        # Pegando chave do layout
        
        while True:
            # Button Values
            button, value = form.Read()
        
            # Check Press Button Values
            if button == 'c':
                Result = ''
                form.FindElement('input').Update(Result)
            elif button == '«':
                Result = Result[:-1]
                form.FindElement('input').Update(Result)
            elif len(Result) == 16:
                pass
        
        # Results
            elif button == '=':
                Result = form.FindElement('input').get()
                Answer = Calculator.calculate(Result)
                try:
                    Answer = str(round(float(Answer), 3))
                except TypeError:
                    sleep(2)
                    Answer = ''
                                       
                form.FindElement('input').Update(Answer)
                Result = Answer
        
            # close the window
            elif button == 'Quit' or button == None:
                break
            else:
                Result += button
                form.FindElement('input').Update(Result)
   
    
        


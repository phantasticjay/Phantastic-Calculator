import PySimpleGUI as sg
import math

sg.theme('Black')  # Using a dark mode theme for this project

layout = [[sg.Input(justification='right', font=[30], key='input', size=(5, 5), expand_x=True, background_color='black')],
          [sg.Button('C', button_color='#777777'), sg.Button('%', button_color='#777777'), sg.Button('DEL', button_color='#777777')],
          [sg.Button('¹/x'), sg.Button('x²'), sg.Button('√'), sg.Button('÷', button_color='#FF6666')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('x', button_color='#FF6666')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-', button_color='#FF6666')],
          [sg.Button('log'), sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+', button_color='#FF6666')],
          [sg.Button('ln'), sg.Button('0', expand_x=True), sg.Button('.'), sg.Button('=', button_color='#FF6666')]]

window = sg.Window('Phantastic Calculator', layout, auto_size_buttons=False,
                   default_button_element_size=(7, 3), element_justification='right',
                   button_color=('white', '#333333'))

keys_entered = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # Calculator can only be closed with the X on the window
        break
    if event == 'C':  # Clears the input of the text box to restart calculator
        keys_entered = ''
    if event == 'DEL':  # Deletes the most recent input
        keys_entered = keys_entered[:-1]
    if event in '1234567890+-x%.÷':  # If any of the buttons are pushed and contain any of these elements, they show up on the text box
        keys_entered = values['input']
        keys_entered += event

    if event == '=':
        keys_enteredFormat = keys_entered.replace('x', '*')  # Replaces the x in the string to a * to make the eval() function work
        keys_enteredFormatv2 = keys_enteredFormat.replace('÷', '/')  # Replaces the ÷ in the string to a / to make the eval() function work
        keys_entered = eval(str(keys_enteredFormatv2))  # Calculates the entire string

    if event == '√':
        keys_entered = math.sqrt(int(keys_entered))

    if event == 'x²':
        keys_entered = int(keys_entered) * int(keys_entered)

    if event == '¹/x':
        keys_entered = 1/int(keys_entered)

    if event == 'log':
        keys_entered = math.log10(int(keys_entered))

    if event == 'ln':
        keys_entered = math.log1p(int(keys_entered))

    window['input'].update(keys_entered)  # Updates the calculator screen

window.close()

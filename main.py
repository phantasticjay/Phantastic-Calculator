import PySimpleGUI as sg

sg.theme('DarkBlack') # Using a dark mode theme for this project

layout = [[sg.Input(size=(15, 1), justification='right', key='input')],
           [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('÷')],
           [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('X')],
           [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
           [sg.Button('0'), sg.Button('.'), sg.Button('C'), sg.Button('-')]]

window = sg.Window('Phantastic Calculator', layout, default_element_size=(5, 2), auto_size_buttons=False)


keys_entered = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'C':
        keys_entered = ''
    elif event in '1234567890':
        keys_entered = values['input']
        keys_entered += event
    window['input'].update(keys_entered)

window.close()

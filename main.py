import PySimpleGUI as sg

sg.theme('DarkBlack') # Using a dark mode theme for this project

layout = [ [sg.Text('Temporary Screen')],
           [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('÷')],
           [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('X')],
           [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
           [sg.Button('0'), sg.Button('.'), sg.Button('C'), sg.Button('-')]]

window = sg.Window('Phantastic Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
window.close()

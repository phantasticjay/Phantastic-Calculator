import PySimpleGUI as sg


def calcSum(num1, num2):  # Function to sum the first input and the input after
    return num1 + num2


def calcSub(num1, num2):  # Function to subtract the first input and the input after
    return num1 - num2


def calcDiv(num1, num2):  # Function to divide the first input and the input after
    return num1 / num2


def calMulti(num1, num2):  # Function to multiply the first input and the input after
    return num1 * num2


def calMod(num1, num2):  # Function to modulo the first input and the input after
    return num1 % num2


sg.theme('DarkBlack') # Using a dark mode theme for this project

layout = [[sg.Input(size=(15, 6), justification='right', key='input')],
           [sg.Button('C'), sg.Button('%'), sg.Button('DEL'), sg.Button('÷')],
           [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('X')],
           [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
           [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
           [sg.Button('0', size=(16,3)), sg.Button('.'), sg.Button('=')]]

window = sg.Window('Phantastic Calculator', layout, default_element_size=(5, 2), auto_size_buttons=False, default_button_element_size= (7,3), element_justification='right')


keys_entered = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # Calculator can only be closed with the X on the window
        break
    if event == 'C': # Clears the input of the text box to restart calculator
        keys_entered = ''
    if event == 'DEL': # Deletes the most recent input
        keys_entered = keys_entered[:-1]
    if event in '1234567890+-X%.÷': # If any of the buttons are pushed and contain any of these elements, they show up on the text box
        keys_entered = values['input']
        keys_entered += event
        count = 0

    if event == '=': # Place holder equal sign to test if it works
        keys_entered = int(keys_entered) * 2

    window['input'].update(keys_entered)

window.close()

import PySimpleGUI as sg

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
    if event == 'C':  # Clears the input of the text box to restart calculator
        keys_entered = ''
    if event == 'DEL':  # Deletes the most recent input
        keys_entered = keys_entered[:-1]
    if event in '1234567890+-X%.÷': # If any of the buttons are pushed and contain any of these elements, they show up on the text box
        keys_entered = values['input']
        keys_entered += event

    if event == '=':
        if '+' in keys_entered:  # Finds if the calculator contains any input of the + sign
            keyList = keys_entered.split('+')  # Splits the calculator input into a list by the + sign so only numbers remain
            print(keyList)
            add = 0
            for i in range(len(keyList)):
                add = add + int(keyList[i])  # Using a for loop to sum the numbers in the list

            keys_entered = add  # Displays the result onto the calculator screen

        elif '-' in keys_entered:  # Finds if the calculator contains any input of the - sign
            keyList = keys_entered.split('-')  # Splits the calculator input into a list by the - sign so only numbers remain
            print(keyList)
            sub = int(keyList[0])
            for i in range(1, len(keyList)):
                sub = sub - int(keyList[i])  # Using a for loop to subtract the numbers in the list

            keys_entered = sub  # Displays the result onto the calculator screen

        elif 'X' in keys_entered:  # Finds if the calculator contains any input of the X sign
            keyList = keys_entered.split('X')  # Splits the calculator input into a list by the X sign so only numbers remain
            print(keyList)
            multi = int(keyList[0])
            for i in range(1, len(keyList)):
                multi = multi * int(keyList[i])  # Using a for loop to multiply the numbers in the list

            keys_entered = multi  # Displays the result onto the calculator screen

        elif '%' in keys_entered:  # Finds if the calculator contains any input of the % sign
            keyList = keys_entered.split('%')  # Splits the calculator input into a list by the % sign so only numbers remain
            print(keyList)
            mod = int(keyList[0])
            for i in range(1, len(keyList)):
                mod = mod % int(keyList[i])  # Using a for loop to modulo the numbers in the loop

            keys_entered = mod  # Displays the result onto the calculator screen

        elif '÷' in keys_entered:  # Finds if the calculator contains any input of the ÷ sign
            keyList = keys_entered.split('÷')  # Splits the calculator input into a list by the ÷ sign so only numbers remain
            print(keyList)
            div = int(keyList[0])
            for i in range(1, len(keyList)):
                div = div / int(keyList[i])  # Using a for loop to divide the numbers in the list

            keys_entered = div  # Displays the result onto the calculator screen

    window['input'].update(keys_entered)  # Updates the calculator screen

window.close()

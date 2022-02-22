from read_data import check_details
import PySimpleGUI as sg


sg.theme('BrightColors')

def home_window():
    layout = [
        [sg.Text('')],[sg.Text('Select a method')],[sg.Text('')],
        [sg.Radio('Select Excel File', "RADIO1", default=True, key="-SL_EXCEL-")],
        [sg.Radio('Add data manually', "RADIO1", default=False, key="-SL_MANUAL-")],
        [sg.Text('')],
        [[sg.Button('Next'), sg.Button('Exit')]]
    ]

    window = sg.Window('Home', layout)

    event, values = window.read()
    if event == 'Exit' or sg.WIN_CLOSED or None:
        state = 'Exit'
        window.close()
    elif event == 'Next':
        if values['-SL_EXCEL-'] == True:
            window.close()
            state = 'Excel'
        elif values['-SL_MANUAL-'] == True:
            window.close()
            state = 'Manual'
    data = None

    return state, data

def select_file_window():

    layout = [[ sg.Text(key='-MSG-', text_color='red',font='Helvitica 16 bold'),],
            [sg.Text('Select Excel file')],
            [sg.Input(key='-IN_FILE-'),sg.FileBrowse(key="-IN_FILE-"),],
            [sg.Text('The file should contain X values in first column and', text_color='gray', font='Helvitica 10')],
            [sg.Text('Y values in second column', text_color='gray', font='Helvitica 10')],
            [sg.Text('')],
            [sg.Text("Select type of graph")],
            [sg.T("   "), sg.Radio('Bar', "RADIO1", default=True, key="-IN_CHART-")],
            [sg.T("   "), sg.Radio('Plot', "RADIO1", default=False)],[sg.Text('')],
            [sg.Button('Next'), sg.Button('Back')]]

    window = sg.Window('EXCEL to Graph', layout)
    msg = ''

    while True:
        event, values = window.read()
        # print(event, values)
        if event == 'Back':
            state = 'Home'
            data = None
            window.close()
        
        if event == sg.WIN_CLOSED:
            quit()
        if event == 'Next':
            if values['-IN_FILE-'] == '' or values['-IN_FILE-'] == None:
                msg = 'Select an excel file!'
                window['-MSG-'].update(msg)
                continue
            if values["-IN_CHART-"] == True:
                chart = 'bar'
            elif values["-IN_CHART-"] == False:
                chart = 'plot'
            file_path = values['-IN_FILE-']
            state = 'Sheets'
            data = {'file_path':file_path, 'chart_type':chart}
        window.close()
        return (state, data)

def sheet_selection_window(sheet_names):

    layout = [[sg.Text(key='-MSG-',text_color='red',font='Helvitica 14 bold')],[sg.Text('Select a sheet from below list')],
            [[sg.T(""), sg.Radio(sheet_name, "RADIO1", default=False, key=sheet_name)] for sheet_name in sheet_names],
            [sg.Text('')],
            [sg.Button('Submit'), sg.Button('Back')]]

    window = sg.Window('Select a Sheet', layout)
    msg = ''

    while True:
        event, values = window.read()
        # print(event, values)
        if event == 'Back':
            window.close()
            return 'Excel', None
        if event == sg.WIN_CLOSED:
            quit()
        if event == 'Submit':
            for key, value in values.items():
                if value == True:
                    window.close()
                    return 'Read', key
        msg = 'Please select a Sheet!'
        window['-MSG-'].update(msg)
        msg = ''

def error_window():

    layout = [
            [sg.Text('')],
            [sg.Text('Not able to read sheet. Please check file',key='-MSG-', background_color = 'red',text_color='black', font='Helvitica 14 bold')],
            [sg.Text('')],
            [sg.Button('Back'), sg.Button('Exit')]]

    window = sg.Window('ERROR!', layout)

    # while True:  # Event Loop
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        quit()
    if event == 'Back':
        window.close()
        return 'Excel'
    return 'Exit'

def details_of_data():
    layout = [[ sg.Text(key='-MSG-', text_color='red',font='Helvitica 16 bold'),],
            [sg.Text('Please check details entered')],
    [sg.Text('X - axis'), sg.InputText(size = (20,1))],
    [sg.Text('Y - axis'), sg.InputText(size = (20,1))],
    [sg.Text('Number of entries'), sg.InputText(size = (5,1))],
    [sg.T("   ")],
    [sg.Text("Select type of graph")],
    [sg.T("   "), sg.Radio('Bar', "RADIO1", default=True, key="-IN_CHART-")],
    [sg.T("   "), sg.Radio('Plot', "RADIO1", default=False)],[sg.Text('')],
    [sg.Button('Next'), sg.Button('Back')]
    ]

    window = sg.Window('Details', layout)
    msg = ''
    while True:
        event, values = window.read()
        if event == 'Back':
            window.close()
            return 'Home', None
        elif event == 'Next':
            if values["-IN_CHART-"] == True:
                chart = 'bar'
            elif values["-IN_CHART-"] == False:
                chart = 'plot'
            if check_details(values):
                details = {'x':values[0], 'y':values[1], 'Number_of_entries': int(values[2]), 'chart':chart}
                window.close()
                return 'Add_Data', details
            else:
                msg = 'Enter correct values'
                window['-MSG-'].update(msg)

def add_maunal_data(msg, data, count):

    msg_ = [key + ' : ' + str(value) for key, value in data.items()]
    msg_ = 'Total Number of Entries : ' + str(count) + '\n' + '\n'.join(msg_)

    layout = [
        [sg.Text(msg, key='-MSG-', text_color='red',font='Helvitica 12 bold')],
        [sg.Text(msg_, text_color='green',font='Helvitica 12 bold')],
        [sg.Text('X value'), sg.InputText()],
        [sg.Text('Y value'), sg.InputText()],
        [sg.Button('Next'), sg.Button('Abort')]
        ]

    window = sg.Window('Details', layout)

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        quit()
    elif event == 'Abort':
        window.close()
        return 'Home', [None, None]
    elif event == 'Next':
        window.close()
        return 'Data_entered', [values[0], values[1]]
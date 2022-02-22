
from itertools import count
from multiprocessing.sharedctypes import Value
from tabnanny import check
from read_data import read_sheet_data, get_sheets, check_entered_data
from windows import select_file_window, sheet_selection_window, error_window, home_window, details_of_data, add_maunal_data
from graph import drow_chart

state = 'Home'
while True:
    # print('state:', state)
    if state == 'Home':
        state, method = home_window()
    elif state == 'Exit':
        quit()

    # Data added Manually
    elif state == 'Manual':
        data_input = {}
        msg = ''
        state, details = details_of_data()
    elif state == 'Add_Data':
        _count = details['Number_of_entries']
        state, [key, value] = add_maunal_data(msg, data_input, _count)
        msg = ''
    elif state == 'Data_entered':
        if check_entered_data(key, value):
            data_input[key] = float(value)
        else:
            msg = 'Not entered a correct value '
        state = 'Add_Data'
        if len(data_input) >= _count:
            state = 'Drow_'
    if state == 'Drow_':
        titles = (details['x'], details['y'])
        drow_chart(data_input, titles, details['chart'])
        state = 'Home'
    
    # Data from Excel
    elif state == 'Excel':
        state, data = select_file_window()
        continue
    elif state == 'F_Error':
        state = error_window()
    elif state == 'Sheets':
        file_path = data['file_path']
        chart_type = data['chart_type']
        sheets, wb_obj = get_sheets(file_path)
        if sheets == 'F_Error':
            state = 'F_Error'
            continue
        state = 'Sheet'
        continue
    elif state == 'Sheet':
        state, sheet =  sheet_selection_window(sheets)
    elif state == 'Read':
        sheet_obj = wb_obj[sheet]
        _data, titles = read_sheet_data(sheet_obj)
        drow_chart(_data, titles, chart_type)
        state = 'Home'

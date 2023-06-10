# while True:
#     print('Welcome to OT amount generator for University of Peradeniya Employees!')
#     option = input('Enter Y for Name if you are from DOFA or Enter N for Basic Salary (Y/N): ')

#     if option.lower() == 'y':
#         ot_hours = None
#         while True:
#             ot_input = input('Enter OT hours: ')
#             try:
#                 ot_hours = float(ot_input)
#                 break
#             except ValueError:
#                 print('Invalid input. Please enter a valid number for OT hours.')

#         name = input('Enter your Name:  ')

#         name_found = False
#         if name.lower() == 'nipuna':
#             ot_amount = (33425 * ot_hours) / 16
#             print(f'Your OT amount is {ot_amount}')
#             name_found = True
#         elif name.lower() == 'deepani':
#             ot_amount = (33425 * ot_hours) / 16
#             print(f'Your OT amount is {ot_amount}')
#             name_found = True
#         elif name.lower() == 'sunil':
#             ot_amount = (33425 * ot_hours) / 16
#             print(f'Your OT amount is {ot_amount}')
#             name_found = True

#         if not name_found:
#             print('Name not found')

#     elif option.lower() == 'n':
#         valid_input = False
#         while not valid_input:
#             basic_salary_input = input('Enter your Basic Salary: ')
#             if basic_salary_input.isnumeric() or (basic_salary_input.startswith('-') and basic_salary_input[1:].isnumeric()):
#                 basic_salary = float(basic_salary_input)
#                 valid_input = True
#             else:
#                 print('Invalid character. Please enter a number for Basic Salary.')

#         ot_hours = None
#         while True:
#             ot_input = input('Enter OT hours: ')
#             try:
#                 ot_hours = float(ot_input)
#                 break
#             except ValueError:
#                 print('Invalid input. Please enter a valid number for OT hours.')

#         ot_amount = (basic_salary * ot_hours) / 16
#         print(f'Your OT amount is {ot_amount}')

#     else:
#         print('Invalid input. Please enter N or B')
#         continue

#     break
import tkinter as tk

def calculate_ot_amount():
    option = option_var.get()

    if option.lower() == 'y':
        ot_hours = float(ot_hours_entry.get())
        name = name_entry.get()

        name_found = False
        if name.lower() == 'nipuna':
            ot_amount = (33425 * ot_hours) / 16
            ot_amount_label.config(text=f'Your OT amount is {ot_amount}')
            name_found = True
        elif name.lower() == 'deepani':
            ot_amount = (33425 * ot_hours) / 16
            ot_amount_label.config(text=f'Your OT amount is {ot_amount}')
            name_found = True
        elif name.lower() == 'sunil':
            ot_amount = (33425 * ot_hours) / 16
            ot_amount_label.config(text=f'Your OT amount is {ot_amount}')
            name_found = True

        if not name_found:
            ot_amount_label.config(text='Name not found')

    elif option.lower() == 'n':
        basic_salary = float(basic_salary_entry.get())
        ot_hours = float(ot_hours_entry.get())

        ot_amount = (basic_salary * ot_hours) / 16
        ot_amount_label.config(text=f'Your OT amount is {ot_amount}')

    else:
        ot_amount_label.config(text='Invalid input. Please enter N or B')
# option = input(' ')
# Create the main window
window = tk.Tk()
window.title('Employee OT Calculator')

# Create and place the UI widgets
option_var = tk.StringVar()
option_label = tk.Label(window, text='Enter Y for Name if you are from DOFA or Enter N for Basic Salary (Y/N):')
option_label.pack()

option_entry = tk.Entry(window, textvariable=option_var)
option_entry.pack()

ot_hours_label = tk.Label(window, text='Enter OT hours:')
ot_hours_label.pack()

ot_hours_entry = tk.Entry(window)
ot_hours_entry.pack()

name_label = tk.Label(window, text='Enter your Name:')
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

basic_salary_label = tk.Label(window, text='Enter your Basic Salary:')
basic_salary_label.pack()

basic_salary_entry = tk.Entry(window)
basic_salary_entry.pack()

calculate_button = tk.Button(window, text='Calculate', command=calculate_ot_amount)
calculate_button.pack()

ot_amount_label = tk.Label(window, text='')
ot_amount_label.pack()

# Start the GUI main loop
window.mainloop()

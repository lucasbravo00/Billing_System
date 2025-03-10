# Restaurant Billing System
# Developed in Python with Tkinter
# Allows product selection, cost calculation and receipt generation

# Required imports
from tkinter import *  # Graphical interface
import random  # For generating random receipt numbers
import datetime  # For date and time in receipts
from tkinter import filedialog, messagebox  # For saving receipts

# Global variable for the calculator
operator = ''

# Product price lists
food_prices = [8.99, 7.50, 6.80, 5.20, 7.30, 10.00, 12.50, 9.00, 11.00, 6.50, 5.80]
drink_prices = [1.50, 2.00, 2.20, 3.50, 4.00, 2.50, 2.30, 1.80, 2.00, 2.30, 1.80]
dessert_prices = [3.50, 4.80, 2.00, 3.00, 3.90, 3.40, 5.00, 4.50, 3.60, 2.80, 4.20]


# Functions for the calculator
def click_button(number):
    """Adds digits/operators to the calculator"""
    global operator
    operator = operator + number
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)


def clear():
    """Clears the calculator display content"""
    global operator
    operator = ''
    calculator_display.delete(0, END)


def get_result():
    """Calculates and displays the operation result"""
    global operator

    if not operator.strip():
        return

    try:
        result = str(eval(operator))
    except Exception as e:
        result = "Syntax Error"

    calculator_display.delete(0, END)
    calculator_display.insert(0, result)
    operator = ''


# Main system functions
def check_checkboxes():
    """Enables/disables fields according to selected checkboxes"""
    # Food handling
    x = 0
    for c in food_boxes:
        if food_variables[x].get() == 1:
            food_boxes[x].config(state=NORMAL)
            if food_text[x].get() == '0':
                food_boxes[x].delete(0, END)
                food_boxes[x].focus()
        else:
            food_boxes[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1

    # Drink handling
    x = 0
    for c in drink_boxes:
        if drink_variables[x].get() == 1:
            drink_boxes[x].config(state=NORMAL)
            if drink_text[x].get() == '0':
                drink_boxes[x].delete(0, END)
                drink_boxes[x].focus()
        else:
            drink_boxes[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1

    # Dessert handling
    x = 0
    for c in dessert_boxes:
        if dessert_variables[x].get() == 1:
            dessert_boxes[x].config(state=NORMAL)
            if dessert_text[x].get() == '0':
                dessert_boxes[x].delete(0, END)
                dessert_boxes[x].focus()
        else:
            dessert_boxes[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1


def total():
    """Calculates subtotals, taxes and grand total"""
    # Food subtotal calculation
    food_subtotal = 0
    p = 0
    for quantity in food_text:
        food_subtotal = food_subtotal + (float(quantity.get()) * food_prices[p])
        p += 1

    # Drink subtotal calculation
    drink_subtotal = 0
    p = 0
    for quantity in drink_text:
        drink_subtotal = drink_subtotal + (float(quantity.get()) * drink_prices[p])
        p += 1

    # Dessert subtotal calculation
    dessert_subtotal = 0
    p = 0
    for quantity in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(quantity.get()) * dessert_prices[p])
        p += 1

    # Grand total and tax calculation
    subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    taxes = subtotal * 0.21  # 21% tax
    total = subtotal + taxes

    # Update variables to display on screen
    var_food_cost.set(f'${round(food_subtotal, 2)}')
    var_drink_cost.set(f'${round(drink_subtotal, 2)}')
    var_dessert_cost.set(f'${round(dessert_subtotal, 2)}')
    var_subtotal.set(f'${round(subtotal, 2)}')
    var_taxes.set(f'${round(taxes, 2)}')
    var_total.set(f'${round(total, 2)}')


def receipt():
    """Generates a detailed receipt with selected products"""
    # Clears the text area
    receipt_text.delete(1.0, END)

    # Receipt header with number and date
    receipt_num = f'N# - {random.randint(1000, 9999)}'
    date = datetime.datetime.now()
    receipt_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    receipt_text.insert(END, f'Data:\t{receipt_num}\t\t{receipt_date}\n')
    receipt_text.insert(END, f'*' * 57 + '\n')
    receipt_text.insert(END, 'Items\tQuantity\t\tItem Cost\n')
    receipt_text.insert(END, f'-' * 57 + '\n')

    # List of selected foods
    for i, food in enumerate(food_text):
        if food.get() != '0':
            cost = float(food.get()) * food_prices[i]
            receipt_text.insert(END, f'{foods[i]}\t{food.get()}\t\t${cost:.2f}\n')

    # List of selected drinks
    for i, drink in enumerate(drink_text):
        if drink.get() != '0':
            cost = float(drink.get()) * drink_prices[i]
            receipt_text.insert(END, f'{drinks[i]}\t{drink.get()}\t\t${cost:.2f}\n')

    # List of selected desserts
    for i, dessert in enumerate(dessert_text):
        if dessert.get() != '0':
            cost = float(dessert.get()) * dessert_prices[i]
            receipt_text.insert(END, f'{desserts[i]}\t{dessert.get()}\t\t${cost:.2f}\n')

    # Financial summary
    receipt_text.insert(END, f'-' * 57 + '\n')
    receipt_text.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    receipt_text.insert(END, f'Taxes: \t\t\t{var_taxes.get()}\n')
    receipt_text.insert(END, f'-' * 57 + '\n')
    receipt_text.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    receipt_text.insert(END, f'*' * 57 + '\n')


def save():
    """Saves the receipt to a text file"""
    receipt_info = receipt_text.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(receipt_info)
    file.close()
    messagebox.showinfo('Your receipt has been saved')


def reset():
    """Resets the application to its initial state"""
    # Clears the receipt area
    receipt_text.delete(0.1, END)

    # Resets all values to zero
    for text in food_text:
        text.set('0')

    for text in drink_text:
        text.set('0')

    for text in dessert_text:
        text.set('0')

    # Disables all input fields
    for box in food_boxes:
        box.config(state=DISABLED)

    for box in drink_boxes:
        box.config(state=DISABLED)

    for box in dessert_boxes:
        box.config(state=DISABLED)

    # Unchecks all checkboxes
    for v in food_variables:
        v.set(0)

    for v in drink_variables:
        v.set(0)

    for v in dessert_variables:
        v.set(0)

    # Clears cost fields
    var_food_cost.set('')
    var_drink_cost.set('')
    var_dessert_cost.set('')
    var_subtotal.set('')
    var_taxes.set('')
    var_total.set('')


# Initialize TKinter
application = Tk()

# Window dimensions
application.geometry('1020x630+0+0')

# Window title
application.title('My Restaurant')

# Background color
application.config(bg='burlywood')

# Prevents window maximization
application.resizable(False, False)

# Title panel
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)
title_label = Label(top_panel, text='Billing System', fg='azure4',
                        font=('Dosis', 48), bg='wheat', width=20)
title_label.grid(row=0, column=0)

# Left panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Costs panel
costs_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=23, pady=6)
costs_panel.pack(side=BOTTOM)

# Food panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                        bd=1, relief=FLAT, fg='azure4', pady=10)
food_panel.pack(side=LEFT)

# Drinks panel
drinks_panel = LabelFrame(left_panel, text='Drink', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4', pady=10)
drinks_panel.pack(side=LEFT)

# Desserts panel
desserts_panel = LabelFrame(left_panel, text='Dessert', font=('Dosis', 19, 'bold'),
                            bd=1, relief=FLAT, fg='azure4', pady=10)
desserts_panel.pack(side=LEFT)

# Right panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='tan')
calculator_panel.pack()

# Receipt panel
receipt_panel = Frame(right_panel, bd=1, relief=FLAT, bg='tan')
receipt_panel.pack()

# Buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='tan')
buttons_panel.pack()

# List for Checkbuttons
foods = ["Pizza", "Hamburger", "Tacos", "Salad", "Pasta", "Sushi", "Paella", "Roast Chicken", "Lasagna", "Burritos", "Croquettes"]
drinks = ["Water", "Coca-Cola", "Orange Juice", "Beer", "Red Wine", "Lemonade", "Iced Tea", "Coffee", "Fanta", "Sprite", "Mineral Water"]
desserts = ["Ice Cream", "Chocolate Cake", "Cookies", "Fresh Fruit", "Apple Pie", "Flan", "Tiramisu", "Cheesecake", "Brownie", "Pudding", "Macarons"]


# Display Food Checkbuttons
food_variables = []
food_boxes = []
food_text = []
counter = 0
for food in foods:

    # Checkbuttons
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=('Dosis', 10, 'bold'), onvalue=1, offvalue=0,
                       variable=food_variables[counter], command=check_checkboxes, pady=5)
    food.grid(row=counter, column=0, sticky=W)

    # Entry boxes
    food_boxes.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_boxes[counter] = Entry(food_panel, font=('Dosis', 10, 'bold'),
                                bd=1, width=6, state=DISABLED, textvariable=food_text[counter])
    food_boxes[counter].grid(row=counter, column=1)
    counter += 1

# Display Drink Checkbuttons
drink_variables = []
drink_boxes = []
drink_text = []
counter = 0
for drink in drinks:

    # Checkbuttons
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drinks_panel, text=drink.title(), font=('Dosis', 10, 'bold'), onvalue=1, offvalue=0,
                        variable=drink_variables[counter], command=check_checkboxes, pady=5)
    drink.grid(row=counter, column=0, sticky=W)

    # Entry boxes
    drink_boxes.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_boxes[counter] = Entry(drinks_panel, font=('Dosis', 10, 'bold'),
                                 bd=1, width=6, state=DISABLED, textvariable=drink_text[counter])
    drink_boxes[counter].grid(row=counter, column=1)
    counter += 1

# Display Dessert Checkbuttons
dessert_variables = []
dessert_boxes = []
dessert_text = []
counter = 0
for dessert in desserts:

    # Checkbuttons
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(desserts_panel, text=dessert.title(), font=('Dosis', 10, 'bold'), onvalue=1, offvalue=0,
                          variable=dessert_variables[counter], command=check_checkboxes, pady=5)
    dessert.grid(row=counter, column=0, sticky=W)

    # Entry boxes
    dessert_boxes.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_boxes[counter] = Entry(desserts_panel, font=('Dosis', 10, 'bold'),
                                   bd=1, width=6, state=DISABLED, textvariable=dessert_text[counter])
    dessert_boxes[counter].grid(row=counter, column=1)
    counter += 1

# Costs panel
var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()

# Food label
food_cost_label = Label(costs_panel,
                         text='Food cost',
                         font=('Dosis', 12, 'bold'),
                         bg='azure4',
                         fg='white',)
food_cost_label.grid(row=0, column=0)

food_cost_text = Entry(costs_panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_food_cost)
food_cost_text.grid(row=0, column=1, padx=41)

# Drink label
drink_cost_label = Label(costs_panel,
                          text='Drink cost',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white',)
drink_cost_label.grid(row=3, column=0)

drink_cost_text = Entry(costs_panel,
                         font=('Dosis', 12, 'bold'),
                         bd=1,
                         width=10,
                         state='readonly',
                         textvariable=var_drink_cost)
drink_cost_text.grid(row=3, column=1, padx=50)

# Dessert label
dessert_cost_label = Label(costs_panel,
                            text='Dessert cost',
                            font=('Dosis', 12, 'bold'),
                            bg='azure4',
                            fg='white',)
dessert_cost_label.grid(row=6, column=0)

dessert_cost_text = Entry(costs_panel,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_dessert_cost)
dessert_cost_text.grid(row=6, column=1, padx=41)

# Subtotal label
subtotal_label = Label(costs_panel,
                        text='Subtotal',
                        font=('Dosis', 12, 'bold'),
                        bg='azure4',
                        fg='white',)
subtotal_label.grid(row=0, column=2)

subtotal_text = Entry(costs_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
subtotal_text.grid(row=0, column=3, padx=41)

# Taxes label
taxes_label = Label(costs_panel,
                     text='Taxes',
                     font=('Dosis', 12, 'bold'),
                     bg='azure4',
                     fg='white')
taxes_label.grid(row=3, column=2)

taxes_text = Entry(costs_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_taxes)
taxes_text.grid(row=3, column=3, padx=41)

# Total label
total_label = Label(costs_panel,
                     text='Total',
                     font=('Dosis', 12, 'bold'),
                     bg='azure4',
                     fg='white',)
total_label.grid(row=6, column=2)

total_text = Entry(costs_panel,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
total_text.grid(row=6, column=3, padx=41)

# Buttons
buttons = ['Total', 'Receipt', 'Save', 'Reset']
created_buttons = []
columns = 0

for button in buttons:
    button = Button(buttons_panel, text=button.title(), font=('Dosis', 10, 'bold'), fg='white',
                   bg='azure4', bd=2, width=11, padx=2)
    created_buttons.append(button)
    button.grid(row=0, column=columns)
    columns += 1

created_buttons[0].config(command=total)
created_buttons[1].config(command=receipt)
created_buttons[2].config(command=save)
created_buttons[3].config(command=reset)

receipt_text = Text(receipt_panel, font=('Dosis', 12, 'bold'), bd=1, width=44, height=17)
receipt_text.grid(row=0, column=0)

# Calculator
calculator_display = Entry(calculator_panel, font=('Dosis', 12, 'bold'), width=44, bd=1)
calculator_display.grid(row=0, column=0, columnspan=5)

calculator_buttons = ['7', '8', '9', '÷', '4', '5', '6', 'x', '1', '2', '3', '-', 'CE', '0', '=', '+']
row = 1
column = 0
saved_buttons = []

for button_text in calculator_buttons:
    # If the button is the division symbol, make it larger. Otherwise it's too small
    if button_text == '÷':
        button = Button(calculator_panel, text=button_text, font=('Dosis', 13, 'bold'), fg='white',
                       bg='azure4', bd=2, width=9)
    else:
        # For other buttons, the font size is the same
        button = Button(calculator_panel, text=button_text.upper(), font=('Dosis', 12, 'bold'), fg='white',
                       bg='azure4', bd=2, width=9)

    button.grid(row=row, column=column)
    saved_buttons.append(button)

    # Update rows and columns
    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

# Assign functionality to buttons
saved_buttons[0].config(command=lambda: click_button('7'))
saved_buttons[1].config(command=lambda: click_button('8'))
saved_buttons[2].config(command=lambda: click_button('9'))
saved_buttons[3].config(command=lambda: click_button('/'))
saved_buttons[4].config(command=lambda: click_button('4'))
saved_buttons[5].config(command=lambda: click_button('5'))
saved_buttons[6].config(command=lambda: click_button('6'))
saved_buttons[7].config(command=lambda: click_button('*'))
saved_buttons[8].config(command=lambda: click_button('1'))
saved_buttons[9].config(command=lambda: click_button('2'))
saved_buttons[10].config(command=lambda: click_button('3'))
saved_buttons[11].config(command=lambda: click_button('-'))
saved_buttons[12].config(command=clear)
saved_buttons[13].config(command=lambda: click_button('0'))
saved_buttons[14].config(command=get_result)
saved_buttons[15].config(command=lambda: click_button('+'))


# Prevent window from closing
application.mainloop()
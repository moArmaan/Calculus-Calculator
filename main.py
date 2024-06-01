import tkinter as tk
import sympy as sp
import math
# Create the main window
calculation = ""
def open_calculator():
    
    def add_to_calculation(symbol):
        global calculation
        calculation += str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    def evaluate_calculation():
        global calculation
        try:
            calculation = str(eval(calculation))
            text_result.delete(1.0,"end")
            text_result.insert(1.0,calculation)
        except:
            clear_field()
            text_result.insert(1.0, "Error")
            pass
    def clear_field(symbol):
        global calculation
        calculation=""
        text_result.insert(1.0, "end")

    def div_to_calculation(symbol):
        pass

    root = tk.Tk()
    root.geometry("300x275")

    text_result = tk.Text(root, height=2, width=16, font=("Arial",24))
    text_result.grid(columnspan=5)

    btn_1 = tk.Button(root, text="1", command = lambda:add_to_calculation(1), width=5,font=("Ariel", 14))
    btn_1.grid(row=2,column=1)

    btn_2 = tk.Button(root, text="2", command = lambda:add_to_calculation(2), width=5,font=("Ariel", 14))
    btn_2.grid(row=2,column=2)

    btn_3= tk.Button(root, text="3", command = lambda:add_to_calculation(3), width=5,font=("Ariel", 14))
    btn_3.grid(row=2,column=3)

    btn_4 = tk.Button(root, text="4", command = lambda:add_to_calculation(4), width=5,font=("Ariel", 14))
    btn_4.grid(row=3,column=1)

    btn_5 = tk.Button(root, text="5", command = lambda:add_to_calculation(5), width=5,font=("Ariel", 14))
    btn_5.grid(row=3,column=2)

    btn_6 = tk.Button(root, text="6", command = lambda:add_to_calculation(6), width=5,font=("Ariel", 14))
    btn_6.grid(row=3,column=3)

    btn_7 = tk.Button(root, text="7", command = lambda:add_to_calculation(7), width=5,font=("Ariel", 14))
    btn_7.grid(row=4,column=1)

    btn_8 = tk.Button(root, text="8", command = lambda:add_to_calculation(8), width=5,font=("Ariel", 14))
    btn_8.grid(row=4,column=2)

    btn_9 = tk.Button(root, text="9", command = lambda:add_to_calculation(9), width=5,font=("Ariel", 14))
    btn_9.grid(row=4,column=3)

    btn_0 = tk.Button(root, text="0", command = lambda:add_to_calculation(0), width=5,font=("Ariel", 14))
    btn_0.grid(row=5,column=2)

    btn_plus = tk.Button(root, text="+", command=lambda:add_to_calculation(("+")), width=5,font=("Ariel", 14))
    btn_plus.grid(row=2,column=4)

    btn_minus = tk.Button(root, text="-", command=lambda:add_to_calculation(("-")), width=5,font=("Ariel", 14))
    btn_minus.grid(row=3,column=4)

    btn_div = tk.Button(root, text="/", command=lambda:add_to_calculation(("/")), width=5,font=("Ariel", 14))
    btn_div.grid(row=4,column=4)

    btn_mul = tk.Button(root, text="*", command=lambda:add_to_calculation(("*")), width=5,font=("Ariel", 14))
    btn_mul.grid(row=5,column=4)

    btn_lbracket = tk.Button(root, text="(", command=lambda:add_to_calculation(("(")), width=5,font=("Ariel", 14))
    btn_lbracket.grid(row=5,column=1)

    btn_rbracket = tk.Button(root, text=")", command=lambda:add_to_calculation((")")), width=5,font=("Ariel", 14))
    btn_rbracket.grid(row=5,column=3)

    button_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11,font=("Ariel", 14))
    button_equals.grid(row=6,columnspan=2, column=3)

    button_clear = tk.Button(root, text="C", command=clear_field, width=11,font=("Ariel", 14))
    button_clear.grid(row=6,columnspan=2, column=1)

    btn_x = tk.Button(root, text="x", command=lambda:add_to_calculation(("x")), width=5,font=("Ariel", 14))
    btn_x.grid(row=7,column=1)

    btn_integrate = tk.Button(root, text="∫", command=lambda:add_to_calculation(("∫")), width=5,font=("Ariel", 14))
    btn_integrate.grid(row=7,column=2)

    root.mainloop()


    root = tk.Tk()
    root.title("Calculator Options")

def open_integral_calculator():
    global text_field
    text_field = None
    root = tk.Tk()
    root.title("Integration by Parts Calculator")
    global global_label 
    global_label = tk.Label(root, text="")
    global_label.grid(row=13,column=0)
    
    def on_text_field_click(entry_number):
    # This function is called when a text field is clicked
        global text_field
        text_field = entry_number
    def on_button_click(char):
    # This function is called when a virtual keyboard button is clicked
        if text_field==1:
            entry_u.insert(tk.END, char)
        elif text_field == 2:
            entry_v.insert(tk.END, char)
    def integrate(u_expression, v_expression):
    # Define the variables and functions
        x = sp.symbols('x')
        u = sp.Function('u')(x)
        v = sp.Function('v')(x)

        ''' Prompt the user for the functions u and dv
        u_expression = input("Enter the expression for u(x): ")
        v_expression = input("Enter the expression for dv (do not include the dx): ")'''



        # Parse the user input and compute du and dv
        try:
            u = sp.sympify(u_expression)
        except:
            print("enter valid input for u")
        try:
            dv = sp.sympify(v_expression)
            
            v = sp.integrate(dv)
        except:
            print("enter valid input for v")
        du = sp.diff(u, x)

        integral_by_parts = u*v - sp.integrate(v * du, x)
        

        # Display the result
        return integral_by_parts
    
    def evaluate_integral():
        global label
        u_func = str(entry_u.get())
        v_func = str(entry_v.get())
        integral = integrate(u_func, v_func)
        answer = sp.pprint(integral, use_unicode=True, wrap_line=False) 
        label_value = global_label.cget("text")
        global_label.config(text = "")
        global_label.config(text= integral)
    # Create the main window
    
    
    

    #entry fields for u(x) and v(x)
    label = tk.Label(root, text="Enter u(x):")
    label.grid(row=2, column=2)
    entry_u = tk.Entry(root, width=30)
    entry_u.grid(row = 2, column=3)
    entry_u.bind("<Button-1>", lambda event, entry_number=1: on_text_field_click(entry_number))
    

    label = tk.Label(root, text="Enter v(x):")
    label.grid(row=3,column=2)
    entry_v = tk.Entry(root, width=30)
    entry_v.grid(row=3,column=3)
    entry_v.bind("<Button-1>", lambda event, entry_number=2: on_text_field_click(entry_number))

    row_val = 4
    col_val = 0
    keyboard_inputs = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '=', '+']
    for char in keyboard_inputs:
        if char != '=':
            tk.Button(root, text=char, width=5, command=lambda c=char: on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
        elif char=='=':
            tk.Button(root, text=char, width=5, command=lambda: evaluate_integral()).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1

        if col_val > 3:
            col_val = 0
            row_val += 1 
    scientific_keyboard_inputs = ['x','π', 'e', 'sin','cos','tan','arcsin','arccos','arctan','(',')','^','!','√','∛']
    for char in scientific_keyboard_inputs:
        tk.Button(root, text=char, width=5, command=lambda c=char: on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)
        if char == 'π':
            tk.Button(root, text='π', width=5, command=lambda c='pi': on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)
        if char == 'e':
            tk.Button(root, text='e', width=5, command=lambda c='E': on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)
        if char == 'arcsin' or char =='arccos' or char == 'arctan':
            if char == 'arcsin':
                sym = 'asin('
            elif char =='arccos':
                sym ='acos('
            elif char == 'arctan':
                sym='atan('
            tk.Button(root, text=char, width=5, command=lambda c=sym: on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)

        if char == '^':
            tk.Button(root, text='^', width=5, command=lambda c='**': on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)

            
        
        if char == 'sin' or char == 'cos' or char == 'tan':
            char = char + '('
            tk.Button(root, text=char, width=5, command=lambda c=char: on_button_click(c)).grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1 
    



root = tk.Tk()
root.title("Calculator Options")
# Create buttons for each option
calculator_button = tk.Button(root, text="Basic Calculator", command=open_calculator)
calculator_button.pack(pady=10)

integral_button = tk.Button(root, text="Integral Calculator", command=open_integral_calculator)
integral_button.pack(pady=10)

'''series_button = tk.Button(root, text="Series Calculator", command=open_series_calculator)
series_button.pack(pady=10)

volume_button = tk.Button(root, text="Volume Calculator", command=open_volume_calculator)
volume_button.pack(pady=10)'''

# Run the Tkinter event loop
root.mainloop()
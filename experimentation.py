'''import sympy as sp

# Define the variables and functions
x = sp.symbols('x')
u = sp.Function('u')(x)
v = sp.Function('v')(x)

# Prompt the user for the functions u and dv
u_expression = input("Enter the expression for u(x): ")
v_expression = input("Enter the expression for dv (do not include the dx): ")


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

integral_by_parts = u*v - sp.integrate(v * du, x)'''

# Display the result
'''print("Integral of u * dv:") 
sp.pretty_print(integral)'''
'''print("\nIntegral by parts:")
sp.pretty_print(integral_by_parts)'''

import tkinter as tk
from tkinter import *

root = tk.Tk()

#create an input field
u_x = Entry(root)
u_x.pack()

root.mainloop()

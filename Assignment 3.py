# Program Name: Assignment3.py
# Course: IT3883/Section 3883
# Student Name: Michael Glover
# Assignment Number: Assignment 3
# Due Date: 03/06/2026
# Purpose: Make a GUI application to convert mpg into kilometers per liter
# Resources used: Python tkinter documentation

import tkinter as tk

MPG_TO_KML = 0.425143707


def on_input_change(*args):
    """
    Called automatically whenever the user types in the input field.
    Reads the MPG value, performs the conversion, and updates the result label.
    Handles non-numeric input and blank fields without crashing.
    """
    raw = mpg_var.get()

    
    if raw.strip() == "":
        result_var.set("")
        return

   
    try:
        mpg_value = float(raw)
        kml_value = mpg_value * MPG_TO_KML
        
        result_var.set(f"{kml_value:.6f}")
    except ValueError:
        
        result_var.set("Invalid input")



root = tk.Tk()
root.title("Miles Per Gallon to km/L Converter")
root.resizable(False, False)


root.configure(padx=20, pady=20)


mpg_var = tk.StringVar()
result_var = tk.StringVar()


mpg_var.trace_add("write", on_input_change)


title_insert = tk.Label(root, text="Fuel Converter",
                        font=("Times New Roman", 11, "bold"))
title_insert.grid(row=0, column=0, columnspan=2, pady=(0, 15))


miles_line = tk.Label(root, text="Miles per Gallon :", font=("Times New Roman", 11))
miles_line.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)

miles_entry = tk.Entry(root, textvariable=mpg_var, font=("Times New Roman", 11), width=18)
miles_entry.grid(row=1, column=1, sticky="w", pady=5)
miles_entry.focus()  


kml_line = tk.Label(root, text="Kilometers per Liter :", font=("Times New Roman", 11))
kml_line.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)

result_output = tk.Label(root, textvariable=result_var, font=("Times New Roman", 11, "bold"),
                       fg="blue", anchor="w", width=18)
result_output.grid(row=2, column=1, sticky="w", pady=5)


note_input = tk.Label(root, text="Conversion: 1 mpg = 0.425143707 km/L",
                       font=("Times New Roman", 9), fg="blue")
note_input.grid(row=3, column=0, columnspan=2, pady=(10, 0))


root.mainloop()
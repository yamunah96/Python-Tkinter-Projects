import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())
        
        if weight <= 0 or height_cm <= 0:
            messagebox.showerror("Error", "Please enter valid weight and height (greater than 0).")
            return
        
        height_m = height_cm / 100  # Convert cm to meters
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)
        print(bmi)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        result_label.config(text=f"Age: {entry_age.get()} years\nYour BMI is: {bmi}\nCategory: {category}")
    
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for weight and height.")

def clear_all():
    entry_age.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="Your BMI will appear here!")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator for Kids")
window.configure(bg="#f0f8ff")  # Light blue background
window.geometry("350x350")

# Title label
label_title = tk.Label(window, text="BMI Calculator for Kids", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#333366")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Age
label_age = tk.Label(window, text="Age:", font=("Arial", 10), bg="#f0f8ff")
label_age.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1, padx=10, pady=5)

# Weight
label_weight = tk.Label(window, text="Weight (kg):", font=("Arial", 10), bg="#f0f8ff")
label_weight.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_weight = tk.Entry(window)
entry_weight.grid(row=2, column=1, padx=10, pady=5)

# Height
label_height = tk.Label(window, text="Height (m):", font=("Arial", 10), bg="#f0f8ff")
label_height.grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_height = tk.Entry(window)
entry_height.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=exit, bg="#66ccff", fg="black", font=("Arial", 10))
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Clear button
clear_button = tk.Button(window, text="Clear", command=clear_all, bg="#ff9999", font=("Arial", 10))
clear_button.grid(row=5, column=0, columnspan=2)

# Result label
result_label = tk.Label(window, text="Your BMI will appear here!", font=("Arial", 10), bg="#f0f8ff", fg="#333333", justify="center")
result_label.grid(row=6, column=0, columnspan=2, pady=15)

# BMI categories note
note_label = tk.Label(window, text="Note:\nUnderweight (<18.5), Normal (18.5-24.9),\nOverweight (25-29.9), Obese (30+)", font=("Arial", 8), bg="#f0f8ff")
note_label.grid(row=7, column=0, columnspan=2)

# Start the main loop
window.mainloop()

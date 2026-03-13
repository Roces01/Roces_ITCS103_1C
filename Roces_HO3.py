import tkinter as tk


root = tk.Tk()
root.title("Simple Calculator")


def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    result_label.config(text=f"The sum of {num1} + {num2} is {result}")

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    result_label.config(text=f"The subtraction of {num1} - {num2} is {result}")

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    result_label.config(text=f"The multiplication of {num1} * {num2} is {result}")

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 != 0:
        result = num1 / num2
        result_label.config(text=f"The division of {num1} / {num2} is {result}")
    else:
        result_label.config(text="Cannot divide by zero")


result_label = tk.Label(root, text="Enter numbers and choose operation")
result_label.grid(row=0, column=0, columnspan=2, pady=10)


label1 = tk.Label(root, text="Enter 1st Number:")
label1.grid(row=1, column=0)

label2 = tk.Label(root, text="Enter 2nd Number:")
label2.grid(row=2, column=0)


entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)


btn_add = tk.Button(root, text="Add", command=add)
btn_add.grid(row=3, column=0)

btn_sub = tk.Button(root, text="Subtract", command=subtract)
btn_sub.grid(row=3, column=1)

btn_mul = tk.Button(root, text="Multiply", command=multiply)
btn_mul.grid(row=4, column=0)

btn_div = tk.Button(root, text="Division", command=divide)
btn_div.grid(row=4, column=1)


root.mainloop()

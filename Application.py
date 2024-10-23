import tkinter as tk
from tkinter import ttk


def process_data():
    input1 = entry1.get()
    input2 = entry2.get()
    input3 = entry3.get()
    input4 = entry4.get()

    output_text = f"Input 1: {input1}\nInput 2: {input2}\nInput 3: {input3}\nInput 4: {input4}"
    output_label.config(text=output_text)


root = tk.Tk()
root.title("Data Entry Application")

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

title_label = tk.Label(left_frame, text="Voer data in", font=("Arial", 14))
title_label.pack(pady=10)

entry1 = tk.Entry(left_frame)
entry1.pack(pady=5)

entry2 = tk.Entry(left_frame)
entry2.pack(pady=5)

entry3 = tk.Entry(left_frame)
entry3.pack(pady=5)

entry4 = tk.Entry(left_frame)
entry4.pack(pady=5)

submit_button = tk.Button(left_frame, text="Submit", command=process_data)
submit_button.pack(pady=10)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

output_label = tk.Label(right_frame, text="", font=("Arial", 12), justify=tk.LEFT)
output_label.pack()

root.mainloop()

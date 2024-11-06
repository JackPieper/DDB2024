import tkinter as tk
from tkinter import ttk


def processData():
    input1 = entry1.get()
    input2 = entry2.get()
    input3 = entry3.get()
    input4 = entry4.get()

    outputText = f"i1: {input1}\ni2: {input2}\ni3: {input3}\ni4: {input4}"
    outputLabel.config(text=outputText)


root = tk.Tk()
root.minsize(300, 200)

leftFrame = tk.Frame(root)
leftFrame.pack(side=tk.LEFT, padx=10, pady=10)

titleLabel = tk.Label(leftFrame, text="Voer data in", font=("Arial", 14))
titleLabel.pack(pady=10)

entry1 = tk.Entry(leftFrame)
entry1.pack(pady=5)

entry2 = tk.Entry(leftFrame)
entry2.pack(pady=5)

entry3 = tk.Entry(leftFrame)
entry3.pack(pady=5)

entry4 = tk.Entry(leftFrame)
entry4.pack(pady=5)

submitButton = tk.Button(leftFrame, text="Bevestigen", command=processData)
submitButton.pack(pady=10)

rightFrame = tk.Frame(root)
rightFrame.pack(side=tk.RIGHT, padx=10, pady=10)

outputLabel = tk.Label(rightFrame, text="", font=("Arial", 12), justify=tk.LEFT)
outputLabel.pack()

root.mainloop()
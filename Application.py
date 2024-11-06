import tkinter as tk
import sklearn
import joblib


def processData():
    X = [[]]
    X[0].append(entry1.get())
    X[0].append(entry2.get())
    X[0].append(entry3.get())
    X[0].append(entry4.get())
    X[0].append(entry5.get())
    pred = model.predict(X)

    outputText = f"Resultaat: {pred[0]:.2f} minuten."
    outputLabel.config(text=outputText)

    segments = [30, 20, 50]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]
    canvas = tk.Canvas(root, width=300, height=100)
    canvas.pack()
    left = 10
    for segment, color in zip(segments, colors):
        canvas.create_rectangle(left, 40, left + segment * 3, 70, fill=color)
        left += segment * 3


model = joblib.load('beste_random_forest_model.pkl')

root = tk.Tk()
root.minsize(300, 200)

leftFrame = tk.Frame(root)
leftFrame.pack(side=tk.LEFT, padx=10, pady=10)

titleLabel = tk.Label(leftFrame, text="Voer variabelen in", font=("Arial", 14))
titleLabel.pack(pady=10)

entry1 = tk.Entry(leftFrame)
entry1.insert(0, "progfh_in_duur_clean")
entry1.pack(pady=5)

entry2 = tk.Entry(leftFrame)
entry2.insert(0, "oorz_code")
entry2.pack(pady=5)

entry3 = tk.Entry(leftFrame)
entry3.insert(0, "geo_mld")
entry3.pack(pady=5)

entry4 = tk.Entry(leftFrame)
entry4.insert(0, "prioriteit")
entry4.pack(pady=5)

entry5 = tk.Entry(leftFrame)
entry5.insert(0, "sap_meldtijd")
entry5.pack(pady=5)

submitButton = tk.Button(leftFrame, text="Bevestigen", command=processData)
submitButton.pack(pady=10)

rightFrame = tk.Frame(root)
rightFrame.pack(side=tk.RIGHT, padx=10, pady=10)

outputLabel = tk.Label(rightFrame, text="", font=("Arial", 12), justify=tk.LEFT)
outputLabel.pack()

root.mainloop()
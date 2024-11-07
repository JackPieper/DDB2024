import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np


# Load the trained model once when the script runs
try:
    model = joblib.load('beste_random_forest_model.pkl')
except FileNotFoundError:
    print("Model file not found. Ensure 'beste_random_forest_model.pkl' is in the directory.")
    exit()


def validate_and_get_input():
    """
    Validate and retrieve input values from the entry fields.
    Returns:
        list: A list of validated float values from the input fields.
    """
    try:
        inputs = [
            float(entry1.get()),
            float(entry2.get()),
            float(entry3.get()),
            float(entry4.get()),
            float(entry5.get())
        ]
        return inputs
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
        return None


def display_prediction(prediction, closest_value):
    """
    Display the prediction and closest value on the output label.
    """
    output_text = f"Resultaat: {prediction:.2f} minuten (Closest: {closest_value:.2f} minuten)."
    outputLabel.config(text=output_text)


def draw_probability_bar(leng, total_preds):
    """
    Draws a bar chart on the canvas representing the probability distribution.
    """
    canvas.delete("all")
    segments = [leng, total_preds - leng]
    colors = ["red", "green"]
    left = 10
    for segment, color in zip(segments, colors):
        canvas.create_rectangle(left, 40, left + segment * 3, 70, fill=color)
        left += segment * 3


def process_data():
    """
    Process data: retrieves inputs, makes a prediction, and updates the UI.
    """
    inputs = validate_and_get_input()
    if inputs is None:
        return
    
    X = [inputs]
    
    try:
        # Make prediction
        pred = model.predict(X)[0]

        # Gather predictions from all trees in the ensemble
        all_preds = np.array(sorted(tree.predict(X)[0] for tree in model.estimators_))
        
        # Calculate distribution position and closest value
        leng = np.sum(all_preds < pred)
        closest_value = all_preds[np.abs(all_preds - pred).argmin()]
        
        # Display results and draw probability bar
        display_prediction(pred, closest_value)
        draw_probability_bar(leng, len(all_preds))
    
    except Exception as e:
        messagebox.showerror("Prediction Error", f"An error occurred: {e}")


def set_placeholder(entry, placeholder):
    """Set placeholder text in the entry."""
    entry.insert(0, placeholder)
    entry.config(fg="grey")
    
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


# Initialize the Tkinter root window
root = tk.Tk()
root.minsize(400, 250)
root.title("Random Forest Prediction")

# Left Frame for inputs
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

titleLabel = tk.Label(left_frame, text="Voer variabelen in", font=("Arial", 14))
titleLabel.pack(pady=10)

# Entry fields for inputs with placeholders
entry1 = tk.Entry(left_frame)
set_placeholder(entry1, "progfh_in_duur_clean")
entry1.pack(pady=5)

entry2 = tk.Entry(left_frame)
set_placeholder(entry2, "oorz_code")
entry2.pack(pady=5)

entry3 = tk.Entry(left_frame)
set_placeholder(entry3, "geo_mld")
entry3.pack(pady=5)

entry4 = tk.Entry(left_frame)
set_placeholder(entry4, "prioriteit")
entry4.pack(pady=5)

entry5 = tk.Entry(left_frame)
set_placeholder(entry5, "sap_meldtijd")
entry5.pack(pady=5)

submitButton = tk.Button(left_frame, text="Bevestigen", command=process_data)
submitButton.pack(pady=10)

# Right Frame for output display
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

outputLabel = tk.Label(right_frame, text="", font=("Arial", 12), justify=tk.LEFT)
outputLabel.pack()

canvas = tk.Canvas(right_frame, width=300, height=100)
canvas.pack()

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import json
import matplotlib.pyplot as plt
from datetime import datetime
from mood_utils import save_mood, load_mood_data, plot_mood_trends

# Create the main window
root = tk.Tk()
root.title("Smart Daily Mood Tracker")
root.geometry("400x400")

# Label for the app title
label = tk.Label(root, text="Mood Tracker", font=("Arial", 20))
label.pack(pady=20)

# Dropdown to choose mood
mood_options = ["Happy", "Sad", "Angry", "Neutral"]
selected_mood = tk.StringVar(root)
selected_mood.set(mood_options[0])  # Default to "Happy"

mood_menu = tk.OptionMenu(root, selected_mood, *mood_options)
mood_menu.pack(pady=10)

# Text field for optional note
note_label = tk.Label(root, text="Optional Note (Your Day in a Sentence)")
note_label.pack()

note_entry = tk.Entry(root, width=40)
note_entry.pack(pady=10)

# Save button to log the mood
def save_and_log():
    mood = selected_mood.get()
    note = note_entry.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_mood(mood, note, timestamp)
    messagebox.showinfo("Success", "Mood logged successfully!")
    note_entry.delete(0, tk.END)

save_button = tk.Button(root, text="Save Mood", command=save_and_log)
save_button.pack(pady=10)

# Button to plot mood trends
def show_mood_trends():
    mood_data = load_mood_data()
    if mood_data:
        plot_mood_trends(mood_data)
    else:
        messagebox.showinfo("No Data", "No mood data to plot.")

plot_button = tk.Button(root, text="Show Mood Trends", command=show_mood_trends)
plot_button.pack(pady=10)

root.mainloop()


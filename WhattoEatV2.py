import json
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import webbrowser  # To open a URL in the default browser

# File to store food ideas
FILE_NAME = Path.home() / "Documents" / "food_ideas.json"

# Default food ideas to preload, IF YOU MODIFY THIS PART OF THE CODE, BE SURE TO DELETE THE "FOOD_IDEAS.JSON" FILE FROM THE DOCUMENTS FOLDER ON YOUR COMPUTER SO THAT IT'LL CREATE A NEW ONE WITH YOUR NEW FOODS
DEFAULT_FOOD_IDEAS = [
    {"name": "Pasta", "time_required": 20},
    {"name": "Salad", "time_required": 10},
    {"name": "Grilled Cheese", "time_required": 5},
    {"name": "Sandwich", "time_required": 10}
]


# Load food ideas from file, or create a new list if the file doesn't exist
def load_food_ideas():
    if not FILE_NAME.exists():
        save_food_ideas(DEFAULT_FOOD_IDEAS)  # Initialize with default items
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save food ideas to file
def save_food_ideas(ideas):
    with open(FILE_NAME, "w") as file:
        json.dump(ideas, file)


# Add a new food idea to the list
def input_new_food_idea():
    name = entry_food_name.get()
    time_required = entry_time_required.get()
    if not name or not time_required.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid food name and time.")
        return
    time_required = int(time_required)
    ideas = load_food_ideas()
    ideas.append({"name": name, "time_required": time_required})
    save_food_ideas(ideas)
    messagebox.showinfo("Success", f"Food idea '{name}' added!")


# List food ideas within the time range
def list_food_ideas_within_range():
    time_available = entry_time_available.get()
    if not time_available.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid time.")
        return
    time_available = int(time_available)
    ideas = load_food_ideas()
    matching_ideas = [
        idea for idea in ideas if abs(idea["time_required"] - time_available) <= 15
    ]
    if matching_ideas:
        listbox_food_ideas.delete(0, tk.END)
        for idea in matching_ideas:
            listbox_food_ideas.insert(tk.END, f"{idea['name']} (takes {idea['time_required']} minutes)")
    else:
        messagebox.showinfo("No Matches", "No matching food ideas found within your time range.")


# Open Google Sheets link
def open_contribution_link():
    webbrowser.open(
        "https://docs.google.com/spreadsheets/d/1HnQ-BuLmDDI9-WRNhh6pP_7KkP_EB4VGa7M3NXYe6r8/edit?usp=sharing")


# Create main window
def create_main_window():
    window = tk.Tk()
    window.title("Hitarth's Food Idea Generator")

    label_food_name = tk.Label(window, text="Enter the name of the food:")
    label_food_name.grid(row=0, column=0, padx=10, pady=10)
    global entry_food_name
    entry_food_name = tk.Entry(window, width=30)
    entry_food_name.grid(row=0, column=1, padx=10, pady=10)

    label_time_required = tk.Label(window, text="Enter the time required (in minutes):")
    label_time_required.grid(row=1, column=0, padx=10, pady=10)
    global entry_time_required
    entry_time_required = tk.Entry(window, width=30)
    entry_time_required.grid(row=1, column=1, padx=10, pady=10)

    button_add_food = tk.Button(window, text="Add Food Idea", width=20, command=input_new_food_idea)
    button_add_food.grid(row=2, column=0, columnspan=2, pady=10)

    label_time_available = tk.Label(window, text="Enter your available time (in minutes):")
    label_time_available.grid(row=3, column=0, padx=10, pady=10)
    global entry_time_available
    entry_time_available = tk.Entry(window, width=30)
    entry_time_available.grid(row=3, column=1, padx=10, pady=10)

    button_list_food = tk.Button(window, text="List Food Ideas", width=20, command=list_food_ideas_within_range)
    button_list_food.grid(row=4, column=0, columnspan=2, pady=10)

    label_food_ideas = tk.Label(window, text="Matching Food Ideas Within 15 Minutes:")
    label_food_ideas.grid(row=5, column=0, padx=10, pady=10)

    global listbox_food_ideas
    listbox_food_ideas = tk.Listbox(window, width=50, height=10)
    listbox_food_ideas.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Add "Contribute to Database" button
    button_contribute = tk.Button(window, text="Contribute to Database", width=20, command=open_contribution_link)
    button_contribute.grid(row=7, column=0, columnspan=2, pady=10)

    button_exit = tk.Button(window, text="Exit", width=20, command=window.quit)
    button_exit.grid(row=8, column=0, columnspan=2, pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_main_window()

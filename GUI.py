import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Gui Testing")
root.geometry("500x350")
root.minsize(400, 300)

# Allow resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Main frame (recommended when using ttk)
main_frame = ttk.Frame(root, padding=15)
main_frame.grid(row=0, column=0, sticky="nsew")

# Make frame responsive
for i in range(2):
    main_frame.columnconfigure(i, weight=1)

# ---- Widgets ----

# Label
label = ttk.Label(main_frame, text="Desktop Tool V 1.0 BETA", font=("Segoe UI", 14))
label.grid(row=0, column=0, columnspan=2, pady=10)

# Entry
entry = ttk.Entry(main_frame)
entry.grid(row=5, column=3, sticky="ew", padx=5)
entry.insert(0, "Screenshot Image Destination")

# Button
def on_click():
    label.config(text=f"You typed: {entry.get()}")
    pass

button = ttk.Button(main_frame, text="Desktop Snap", command=on_click)
button.grid(row=1, column=1, sticky="ew", padx=5)

button = ttk.Button(main_frame, text="Submit", command=on_click)
button.grid(row=1, column=0, sticky="ew", padx=5)

# Checkbox
check_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(
    main_frame, text="Enable option", variable=check_var
)
checkbox.grid(row=2, column=0, columnspan=2, pady=5)

# Combobox (dropdown)
combo = ttk.Combobox(
    main_frame,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly"
)
combo.current(0)
combo.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)

# Progress bar
progress = ttk.Progressbar(
    main_frame, mode="determinate", maximum=100
)
progress.grid(row=4, column=0, columnspan=2, sticky="ew", pady=10)
progress["value"] = 50

# Quit button
quit_button = ttk.Button(main_frame, text="Quit", command=root.destroy)
quit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Start the app
root.mainloop()

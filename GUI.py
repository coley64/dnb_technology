import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Enter your name:")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

button = tk.Button(root, text="Submit")
button.grid(row=1, column=0, columnspan=2)

root.mainloop()
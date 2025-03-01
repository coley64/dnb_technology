import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import matplotlib.pyplot as plt

def scan_network():
    target = target_entry.get()
    if not target:
        output_text.insert(tk.END, "Please enter a target IP or range.\n")
        return
    
    output_text.insert(tk.END, f"Scanning {target}...\n")
    try:
        result = subprocess.run(["ping", "-c", "4", target], capture_output=True, text=True)
        output_text.insert(tk.END, result.stdout + "\n")
    except Exception as e:
        output_text.insert(tk.END, f"Error: {e}\n")

def show_graph():
    times = [10, 20, 15, 25]  # Example data (in milliseconds)
    packets = [1, 2, 3, 4]
    
    plt.figure(figsize=(6,4))
    plt.plot(packets, times, marker='o', linestyle='-')
    plt.xlabel("Packet Number")
    plt.ylabel("Response Time (ms)")
    plt.title("Ping Response Times")
    plt.grid()
    plt.show()

# Initialize main window
root = tk.Tk()
root.title("DNB Technology - Network Scanner")
root.geometry("500x450")

# Title Label
title_label = ttk.Label(root, text="DNB Technology - Network Scanner", font=("Arial", 14))
title_label.pack(pady=10)

# Input Field
target_label = ttk.Label(root, text="Enter Target IP / Range:")
target_label.pack()
target_entry = ttk.Entry(root, width=40)
target_entry.pack(pady=5)

# Scan Button
scan_button = ttk.Button(root, text="Start Scan", command=scan_network)
scan_button.pack(pady=10)

# Graph Button
graph_button = ttk.Button(root, text="Show Graph", command=show_graph)
graph_button.pack(pady=10)

# Output Area
output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack(pady=10)

# Run Application
root.mainloop()

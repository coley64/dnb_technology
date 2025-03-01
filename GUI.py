import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading

# Global variables to store ping results
times = []
packets = []

def scan_network():
    target = target_entry.get()
    if not target:
        output_text.insert(tk.END, "Please enter a target IP or range.\n")
        return
    
    output_text.insert(tk.END, f"Scanning {target}...\n")
    times.clear()
    packets.clear()
    
    def ping():
        try:
            for i in range(1, 5):
                result = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
                output_text.insert(tk.END, result.stdout + "\n")
                if "time=" in result.stdout:
                    time_ms = float(result.stdout.split("time=")[1].split(" ")[0])
                    times.append(time_ms)
                    packets.append(i)
                else:
                    times.append(0)
                    packets.append(i)
        except Exception as e:
            output_text.insert(tk.END, f"Error: {e}\n")
    
    threading.Thread(target=ping).start()

def update_graph(frame):
    if packets:
        ax.clear()
        ax.plot(packets, times, marker='o', linestyle='-')
        ax.set_xlabel("Packet Number")
        ax.set_ylabel("Response Time (ms)")
        ax.set_title("Ping Response Times")
        ax.grid()

def show_graph():
    global fig, ax
    fig, ax = plt.subplots(figsize=(6, 4))
    ani = FuncAnimation(fig, update_graph, interval=1000)
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
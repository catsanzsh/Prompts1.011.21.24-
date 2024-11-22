import socket
import tkinter as tk
from tkinter import messagebox, ttk

# Function to scan a single port
def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

# Function to perform a scan
def start_scan():
    target_ip = entry_ip.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    if not target_ip:
        messagebox.showerror("Error", "Please enter a valid IP address.")
        return

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            open_ports.append(port)
            tree.insert("", tk.END, values=(port, "Open"))

    if open_ports:
        messagebox.showinfo("Scan Complete", f"Open ports found: {open_ports}")
    else:
        messagebox.showinfo("Scan Complete", "No open ports found.")

# Setting up the GUI
root = tk.Tk()
root.title("Basic Network Scanner")

# Frame for IP and port entry
frame_entry = tk.Frame(root)
frame_entry.pack(pady=10)

tk.Label(frame_entry, text="Target IP:").grid(row=0, column=0, padx=5, pady=5)
entry_ip = tk.Entry(frame_entry)
entry_ip.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entry, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
entry_start_port = tk.Entry(frame_entry)
entry_start_port.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entry, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
entry_end_port = tk.Entry(frame_entry)
entry_end_port.grid(row=2, column=1, padx=5, pady=5)

# Scan button
btn_scan = tk.Button(root, text="Start Scan", command=start_scan)
btn_scan.pack(pady=10)

# Treeview to display scan results
tree = ttk.Treeview(root, columns=("Port", "Status"), show="headings")
tree.heading("Port", text="Port")
tree.heading("Status", text="Status")
tree.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()

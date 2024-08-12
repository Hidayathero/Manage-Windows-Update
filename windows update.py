import subprocess
import tkinter as tk
from tkinter import messagebox, font as tkfont, scrolledtext

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.stdout.decode('utf-8'), e.stderr.decode('utf-8')

def log_action(text):
    log_box.config(state=tk.NORMAL)
    log_box.insert(tk.END, text + "\n")
    log_box.see(tk.END)
    log_box.config(state=tk.DISABLED)

def disable_windows_update():
    log_action("Running command: sc stop wuauserv")
    stdout, stderr = run_command(["sc", "stop", "wuauserv"])
    if stderr:
        messagebox.showerror("Error", f"Failed to stop Windows Update service: {stderr}")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

    log_action("Running command: sc config wuauserv start=disabled")
    stdout, stderr = run_command(["sc", "config", "wuauserv", "start=disabled"])
    if stderr:
        messagebox.showerror("Error", f"Failed to disable Windows Update service: {stderr}")
    else:
        messagebox.showinfo("Success", "Windows Update has been disabled.")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

def enable_windows_update():
    log_action("Running command: sc config wuauserv start=auto")
    stdout, stderr = run_command(["sc", "config", "wuauserv", "start=auto"])
    if stderr:
        messagebox.showerror("Error", f"Failed to enable Windows Update service: {stderr}")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

    log_action("Running command: sc start wuauserv")
    stdout, stderr = run_command(["sc", "start", "wuauserv"])
    if stderr:
        messagebox.showerror("Error", f"Failed to start Windows Update service: {stderr}")
    else:
        messagebox.showinfo("Success", "Windows Update has been enabled.")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

def disable_driver_update():
    log_action("Running command: sc stop DeviceInstall")
    stdout, stderr = run_command(["sc", "stop", "DeviceInstall"])
    if stderr:
        messagebox.showerror("Error", f"Failed to stop Device Install service: {stderr}")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

    log_action("Running command: sc config DeviceInstall start=disabled")
    stdout, stderr = run_command(["sc", "config", "DeviceInstall", "start=disabled"])
    if stderr:
        messagebox.showerror("Error", f"Failed to disable Device Install service: {stderr}")
    else:
        messagebox.showinfo("Success", "Driver updates have been disabled.")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

def enable_driver_update():
    log_action("Running command: sc config DeviceInstall start=auto")
    stdout, stderr = run_command(["sc", "config", "DeviceInstall", "start=auto"])
    if stderr:
        messagebox.showerror("Error", f"Failed to enable Device Install service: {stderr}")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

    log_action("Running command: sc start DeviceInstall")
    stdout, stderr = run_command(["sc", "start", "DeviceInstall"])
    if stderr:
        messagebox.showerror("Error", f"Failed to start Device Install service: {stderr}")
    else:
        messagebox.showinfo("Success", "Driver updates have been enabled.")
    log_action(f"stdout: {stdout.strip()}")
    log_action(f"stderr: {stderr.strip()}")

def main():
    global log_box

    root = tk.Tk()
    root.title("Manage Updates")
    root.geometry("650x300")
    root.configure(bg="white")

    title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
    button_font = tkfont.Font(family="Helvetica", size=12)

    title_label = tk.Label(root, text="Manage Windows Updates", font=title_font, bg="white", fg="black")
    title_label.pack(pady=20)

    button_frame = tk.Frame(root, bg="white")
    button_frame.pack(side=tk.LEFT, padx=30, pady=10)

    button_width = 20

    disable_windows_button = tk.Button(button_frame, text="Disable Windows Update", command=disable_windows_update,
                                       font=button_font, bg="#e74c3c", fg="white", activebackground="#c0392b", width=button_width)
    disable_windows_button.grid(row=0, column=0, pady=10)

    enable_windows_button = tk.Button(button_frame, text="Enable Windows Update", command=enable_windows_update,
                                      font=button_font, bg="#27ae60", fg="white", activebackground="#229954", width=button_width)
    enable_windows_button.grid(row=1, column=0, pady=10)

    disable_driver_button = tk.Button(button_frame, text="Disable Driver Update", command=disable_driver_update,
                                      font=button_font, bg="#e74c3c", fg="white", activebackground="#c0392b", width=button_width)
    disable_driver_button.grid(row=2, column=0, pady=10)

    enable_driver_button = tk.Button(button_frame, text="Enable Driver Update", command=enable_driver_update,
                                     font=button_font, bg="#27ae60", fg="white", activebackground="#229954", width=button_width)
    enable_driver_button.grid(row=3, column=0, pady=10)

    log_box = scrolledtext.ScrolledText(root, width=60, height=20, state=tk.DISABLED, bg="white", fg="black")
    log_box.pack(side=tk.RIGHT, padx=20, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

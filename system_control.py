import os
import platform
from tkinter import *

# Detect the Operating System
current_os = platform.system()

# Define Functions for Windows and Mac
def Shutdown():
    if current_os == "Windows":
        os.system("shutdown /s /t 0")
    elif current_os == "Darwin":  # 'Darwin' is macOS
        os.system("sudo shutdown -h now")

def Restart():
    if current_os == "Windows":
        os.system("shutdown /r /t 0")
    elif current_os == "Darwin":
        os.system("sudo shutdown -r now")

def Logout():
    if current_os == "Windows":
        os.system("shutdown /l /t 0")
    elif current_os == "Darwin":
        os.system("osascript -e 'tell application \"System Events\" to log out'")

# Create the Main Window
window = Tk()
window.geometry("500x300")
window.title("System Control - Shutdown, Restart, Logout")

# Add a Label
head = Label(window, text="Control Your PC/Mac", font=('Calibri', 18))
head.pack(pady=20)

# Add Buttons
Button(window, text='Shutdown', command=Shutdown, font=('Calibri', 14), bg='pink').pack(pady=10)
Button(window, text='Restart', command=Restart, font=('Calibri', 14), bg='pink').pack(pady=10)
Button(window, text='Logout', command=Logout, font=('Calibri', 14), bg='pink').pack(pady=10)

# Run the Tkinter Event Loop
window.mainloop()

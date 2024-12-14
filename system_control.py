import os
import platform
from tkinter import *
from PIL import Image, ImageTk  # Import Pillow for image support

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
window.geometry("600x400")
window.title("System Control - Shutdown, Restart, Logout")

# Load and Set Background Image
bg_image = Image.open("bg_image.jpeg")  # Replace 'background.jpg' with your image file
bg_image = bg_image.resize((600, 400), Image.LANCZOS)  # Resize the image to fit the window
bg_photo = ImageTk.PhotoImage(bg_image)

 

bg_label = Label(window, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)  # Set the image to cover the entire window

# Add a Label on Top of Background
head = Label(window, text="Control Your PC/Mac", font=('Calibri', 18), bg="lightblue", fg="black")
head.pack(pady=20)

# Add Buttons
button_style = {
    "font": ('Calibri', 14),
    "bg": "pink",
    "fg": "black",
    "activebackground": "lightpink",
    "activeforeground": "black",
    "relief": "raised",
    "bd": 2
}


Button(window, text='Shutdown', command=Shutdown, **button_style).pack(pady=10)
Button(window, text='Restart', command=Restart, **button_style).pack(pady=10)
Button(window, text='Logout', command=Logout, **button_style).pack(pady=10)

# Run the Tkinter Event Loop
window.mainloop()

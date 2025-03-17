import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import os

def capture_image():
   os.system('python run.py')

# Create the main window
root = tk.Tk()
root.title("Emotion Recognition")
root.geometry("400x300")

# Create the heading
heading = tk.Label(root, text="", font=("Arial", 24))
heading.pack(pady=20)

# Create the welcome message
welcome_msg = tk.Label(root, text="Welcome to the Emotion Based Music Recommendation App!", font=("Arial", 14))
welcome_msg.pack(pady=20)

# Create the capture button
capture_button = tk.Button(root, text="Capture Emotion", command=capture_image)
capture_button.pack(pady=10)

# Start the GUI main loop
root.mainloop()

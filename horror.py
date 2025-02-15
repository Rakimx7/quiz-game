import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os
from PIL import Image, ImageTk

# Get the absolute path to the assets folder
BASE_DIR = os.path.join(os.path.expanduser("~"), "Documents", "quiz Jumpscare", "assets")

# Initialize pygame mixer for sound effects
pygame.mixer.init()

def play_jumpscare():
    sound_path = os.path.join(BASE_DIR, "horrorfinal.mp3")  # Updated sound file name
    pygame.mixer.music.stop()  # Stop any existing sound
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    
    # Hide main form completely
    root.withdraw()
    
    # Show scary image
    top = tk.Toplevel(root)
    top.attributes('-fullscreen', True)  # Fullscreen jump scare
    img_path = os.path.join(BASE_DIR, "jumpscare_image.jpg")  # Use the new transparent image
    img = Image.open(img_path)  # Load scary image
    img = img.resize((800, 600))  # Resize image
    img = ImageTk.PhotoImage(img)
    lbl = tk.Label(top, image=img, bg='black')  # Set background to black for better effect
    lbl.image = img
    lbl.pack()
    
    top.update()
    root.after(2000, lambda: [top.destroy(), reset_ui()])  # Keep it on screen for 2 seconds and then reset UI

def reset_ui():
    root.deiconify()  # Restore the main form
    root.configure(bg='white')  # Restore background
    for widget in root.winfo_children():
        widget.configure(bg='white', fg='black')  # Restore widget visibility

def check_answer():
    answer = entry.get()
    if answer.lower() != correct_answer.lower():
        play_jumpscare()
        messagebox.showerror("Game Over", "You failed! Squid Game Eliminated!")
        root.quit()
    else:
        messagebox.showinfo("Success", "You survived this round!")
        next_question()

def next_question():
    global correct_answer
    question, correct_answer = random.choice(questions)
    label.config(text=question)
    entry.delete(0, tk.END)

# List of questions (you can add more)
questions = [
    ("What is 5 + 3?", "8"),
    ("What is the capital of France?", "Paris"),
    ("What color is the sky?", "Blue"),
    ("What is 10 - 4?", "6"),
    ("What is the square root of 16?", "4"),
    ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
    ("sino crush mo?" , "wala"),
    ("naniniwala kaba sa flat earth theory?, oo o hindi lang sagot?" , "hindi"),
]

# GUI setup
root = tk.Tk()
root.title("Squid Game Challenge")
root.geometry("500x300")

label = tk.Label(root, text="Welcome to Squid Game!", font=("Arial", 16), bg="white")
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 14))
submit_button.pack(pady=10)

# Exit button to close the game
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 14), fg="red")
exit_button.pack(pady=10)

next_question()
root.mainloop()

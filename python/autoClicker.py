from pynput.mouse import Controller
import time
import tkinter as tk
import random as rd

mouse = Controller()

# input = input("Write a message: ")

# print("\nYour message was: " + input)

def on_click():
    # num = 
    if(rd.random() < 0.5):
        label1.config(text="Button Clicket!", bg ="pink")
        button1.config(text="you dum, I am smart, hahahhaha!!!", bg="gray")
        root1.title("hej")
    else:
        label1.config(text="Me is back", bg="gray")
        button1.config(text="what?!?!", bg ="pink")

root1 = tk.Tk()
root1.title("TestTitel")
root1.geometry("400x400")
# root.resizable(width= False,height=False)

grid_frame = tk.Frame(root1, bg="lightgray")
grid_frame.pack(fill="y", padx=20)

# Add labels inside the frame using grid
label1 = tk.Label(grid_frame, text="Row 0, Column 0")
label1.grid(row=0, column=0, padx=5, pady=5)

label2 = tk.Label(grid_frame, text="Row 0, Column 1")
label2.grid(row=0, column=1, padx=5, pady=5)

label3 = tk.Label(grid_frame, text="Row 1, Column 0")
label3.grid(row=1, column=0, padx=5, pady=5)

label4 = tk.Label(grid_frame, text="Row 1, Column 1")
label4.grid(row=2, column=4, padx=5, pady=5)

label5 = tk.Label(grid_frame, text="Row 1sgsfdf, Column 1")
label5.grid(row=2, column=3, padx=5, pady=5)

root2 = tk.Tk()
root2.title("TestTitel")
root2.geometry("400x400")

label3 = tk.Label(root2, text="test testsson",bg="pink")
label3.place(x=10,y=1)

button1 = tk.Button(root2, text="Button hej")
button1.place(x=234,y=390)

root2.mainloop()
from pynput.mouse import Controller,Button
from pynput.mouse import Listener
import time
import tkinter as tk
import random as rd
import threading

mouse = Controller()

programStatus = False
recoredStatus = False
listOfPositions = []
listener = None
thread1 = None
clickCount = 0

def startProgram():
    global programStatus, listOfPositions
    if not programStatus :
       programStatus = True
       button1.config(text="Stop",bg="pink")

       thread2 = threading.Thread(target=runRecording,daemon=True)
       thread2.start()
    else:
        programStatus = False
        button1.config(text="Start",bg="White")


def on_click(x, y, button, pressed):
    global clickCount
    if pressed:  # Only record when the button is pressed (not released)
        ##print(f"Mouse clicked at ({x}, {y})")
        clickCount += 1
        label3.config(text="Nummber of Clicks: " + str(clickCount))
        pos = mouse.position
        listOfPositions.append((pos[0], pos[1]))  # Store the coordinates

def startRecored():
    global recoredStatus, listener, thread1, clickCount, listOfPositions
    if not recoredStatus:
        recoredStatus = True
        button2.config(text="Stop", bg="pink")
        clickCount = 0
        listOfPositions = []
        
        # Start Listener in a separate thread
        thread1 = threading.Thread(target=mouseRecorder, daemon=True)
        thread1.start()
    else:
        recoredStatus = False
        button2.config(text="Start", bg="White")
        
        if listener is not None :
            listener.stop()
            clickCount -= 1
            label3.config(text="Nummber of Clicks: " + str(clickCount))
            listOfPositions.pop()
        print(listOfPositions)

def runRecording() :
    global programStatus, timeDelay
    while programStatus :
        for p in listOfPositions :
            # print(p)
            # print((p[0] + round(rd.random()*4-2),p[1]+ round(rd.random()*4-2)))
            mouse.position = (p[0] + round(rd.random()*4-2),p[1]+ round(rd.random()*4-2))
            time.sleep(0.1)
            mouse.click(Button.left, 1)
            delay = 1
            if timeDelay.get() != "" : delay = timeDelay.get()
            time.sleep(float(delay) + rd.random()*0.5)
            if not programStatus :
                break
        timeToWait = 5
        if programStatus :
            for i in range(timeToWait*10) :
                time.sleep(0.1)
                if not programStatus :
                    break
                button1.config(text="Cancel in: " + str(round(float(timeToWait - i/10),1)))
            button1.config(text="Stop",bg="pink")
            if not programStatus : button1.config(text="Start",bg="White")

def mouseRecorder() :
    global listener
    with Listener(on_click=on_click) as listener:
        listener.join()

# Make Window

root = tk.Tk()
root.title("AutoClicker")
root.geometry("200x250")

timeDelay = tk.StringVar()

label1 = tk.Label(root, text="Start Program")
label1.pack(pady=5)

button1 = tk.Button(root, text="Start",command=startProgram)
button1.pack(pady=5)

label2 = tk.Label(root, text="Recored Movment")
label2.pack(pady=5)

label3 = tk.Label(root, text="Nummber of Clicks: " + str(clickCount))
label3.pack(pady=0)

button2 = tk.Button(root, text="Start",command=startRecored)
button2.pack(pady=5)

label4 = tk.Label(root, text="Time Delay")
label4.pack(pady=0)

entry1 = tk.Entry(root, textvariable=timeDelay)
entry1.pack(pady=5)

root.mainloop()